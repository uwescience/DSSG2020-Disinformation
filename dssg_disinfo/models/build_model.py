import numpy as np
import pandas as pd
import io
import os
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only
from datetime import datetime
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import (Embedding, Dense, LSTM, Bidirectional,
                                    Dropout, Activation, Concatenate,
                                    Flatten, Conv1D, MaxPooling1D)
from tensorflow.keras.callbacks import CSVLogger
from tensorflow.keras import (Input, Model, layers)
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import tensorflow as tf

from .model_arch import *
from .get_data import *
from .word_embedding_arch import *

def build_model(model_arch=None, **copacabana):
    """Builds a model using the passed parameters."""
    # Set default parameters
    if (model_arch=='None' or model_arch=='basic'):
        model = build_model_arch(model_arch, copacabana)
        
    elif model_arch == 'multiple':
        nlp_input=Input(shape=[None]) # Input layer for text
        meta_input=Input(shape=(22,)) # Input layer for 22 linguistic feature columns
        nlp_embeddings=Embedding(vocab_size, embedding_dim)(nlp_input)
        nlp_LSTM=LSTM(bidir_num_filters)(nlp_embeddings) # text embeddings LSTM
        x = Concatenate()([nlp_LSTM, meta_input]) # Merge text LSTM with linguistic features
        x = Dense(1, activation='sigmoid')(x) # Output layer
        model=Model(inputs=[nlp_input, meta_input], outputs=[x]) # Final model
        
    elif (model_arch=='word_embedding'):
        model = build_model_arch(model_arch, copacabana)
        #model = create_word_embd_model_arch(model_arch, copacabana)
        
    else:
        print("Wrong model architecture!")
        
    return model

def fit_and_run_embedding_model(bidir_num_filters=64, dense_1_filters=10, vocab_size=10000, embedding_path=None, embedding_dim=300, maxlen=681, epochs=10, model_arch='word_embedding'):
        # Get the paths
        DATA_PATH = os.getenv("DATA_PATH")
        ALL_FEATURES_DATA = os.getenv("ALL_FEATURES_DATA")
        df = pd.read_csv(os.path.join(DATA_PATH, ALL_FEATURES_DATA))
        ### Splitting the data into training and testing
        X = df['article_text'] # article_text
        y = df.label

        training_sentences, testing_sentences, training_labels, testing_labels = train_test_split(X, y, random_state = 42)

        # making y into np arrays
        training_labels_final = np.array(training_labels)
        testing_labels_final = np.array(testing_labels)
        trunc_type='post'
        oov_tok = "<OOV>"

        ###  Tokenizing, padding, and truncating
        tokenizer = Tokenizer(num_words = vocab_size, oov_token=oov_tok)
        tokenizer.fit_on_texts(training_sentences)
        word_index = tokenizer.word_index
        sequences = tokenizer.texts_to_sequences(training_sentences)
        padded = pad_sequences(sequences,maxlen=maxlen, truncating=trunc_type)
        testing_sequences = tokenizer.texts_to_sequences(testing_sentences)
        testing_padded = pad_sequences(testing_sequences,maxlen=maxlen)
        
        embedding_matrix=create_embedding_matrix(embedding_path,
                                        word_index, embedding_dim)
        vocab_size = len(word_index) + 1 # Adding again 1 because of reserved 0 index
        model = keras.Sequential([
            keras.layers.Embedding(vocab_size, embedding_dim,
                                   weights=[embedding_matrix],
                                   input_length=maxlen),
            keras.layers.Bidirectional(keras.layers.LSTM(bidir_num_filters)),
            keras.layers.Dense(dense_1_filters, activation='relu'),
            keras.layers.Dense(1, activation='sigmoid')
        ])
        
        # Print model layers
        print("Model summary:")
        model.summary()

        ###  Put model together and run
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=[tf.keras.metrics.AUC()])

        ###  Fitting and running the model
        num_epochs = epochs
        file_name = datetime.now().strftime('%Y%m%d%H%M%S')+'_'+model_arch+'_'+str(vocab_size)+'_'+str(embedding_dim)+'_'+str(maxlen)+'_'+str(epochs)+'.log'
        csv_logger = CSVLogger(file_name, append=True, separator=';')
        
        history=model.fit(padded, training_labels_final,
                          epochs=num_epochs,
                          validation_data=(testing_padded, testing_labels_final),
                         callbacks=[csv_logger])
        
        return history, model


def compile_model(model, optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=[tf.keras.metrics.AUC()]):
    """ compile model
    """
    # Print model layers
    print("Model summary:")
    model.summary()

    ### VI. Put model together and run
    model.compile(loss=loss, optimizer=optimizer, metrics=metrics)
    
    return model

                     
def fit_and_run_model(model, vocab_size=10000, embedding_dim=300, maxlen=681, epochs=5, model_arch='basic'):
    
    file_name = datetime.now().strftime('%Y%m%d%H%M%S') +'_'+model_arch+'_'+str(vocab_size)+'_'+str(embedding_dim)+'_'+str(maxlen)+'_'+str(epochs)+'.log'
    csv_logger = CSVLogger(file_name, append=True, separator=';')
    
    if model_arch == 'basic':
        
        ## Fetching data and splitting/tokenizing/padding
        (X_train, X_test, y_train, y_test) = get_data_and_split(vocab_size, maxlen)
        
        history = model.fit(X_train, y_train,
                            epochs=epochs,
                            validation_data=(X_test, y_test),
                            callbacks=[csv_logger])
        
    elif model_arch == 'multiple':
        
        nlp_data_train, nlp_data_test, meta_data_train, meta_data_test, y_train, y_test = get_data_and_split(vocab_size, maxlen, multiple=True)
        history = model.fit([[nlp_data_train, meta_data_train]], y_train, 
                            epochs =epochs,
                            validation_data = (nlp_data_test, meta_data_test, y_test),
                           callbacks=[csv_logger])
    else:
        
        print("Wrong model architecture!")
        
    return history, model

def create_embedding_matrix(filepath, word_index, embedding_dim):
    vocab_size = len(word_index) + 1  # Adding again 1 because of reserved 0 index
    embedding_matrix = np.zeros((vocab_size, embedding_dim))
    with open(filepath) as f:
        for line in f:
            l = len(line.split())
            word = line.split()[0]
            vector = line.split()[-embedding_dim:]
            if word in word_index:
                #n = n + 1
                idx = word_index[word] 
                embedding_matrix[idx] = np.array(
                    vector, dtype=np.float32)[:embedding_dim]

    return embedding_matrix