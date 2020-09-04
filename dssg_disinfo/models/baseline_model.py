from .model_arch import *

from tensorflow import keras
from keras.layers.embeddings import Embedding
from tensorflow.keras import layers
from keras.models import Sequential
from keras.layers import Dense, Flatten, LSTM, Bidirectional, Dropout


def create_basic_model_arch(bidir_num_filters=64, dense_1_filters=10, vocab_size=10000, embedding_dim=300, maxlen=681, dropout_rate=0.2, optimizer='adam'):
    ''' Creates a basic model architecture to be used for the baseline 
    model. 
    Parameters
    -----------
    int
        bidir_num_filters - number of bidirectional filters to be used, default is 64
        dense_1_filters - number of dense filters, with default equal to 10
        vocab_size - the size of vocabulary, default of 10000
        embedding_dim - number of word embedding dimensions - 200 or 300
        maxlen - maximum length of the text sample 
        dropout_rate - drop out rate value 
       
    str
        optimizer - optimizer to be used
    Returns
    -------
    obj
        returns model object that can then be fit and run
            
    '''
    
    model = Sequential()
    
    model.add(layers.Embedding(vocab_size, embedding_dim, input_length=maxlen))
    model.add(Bidirectional(LSTM(bidir_num_filters)))
    model.add(layers.Dense(dense_1_filters, activation='relu'))
    model.add(Dropout(rate=dropout_rate))
    model.add(layers.Dense(1, activation='sigmoid'))
    
    model.compile(optimizer=optimizer,
                  loss='binary_crossentropy',
                  metrics=[tf.keras.metrics.AUC()])
    
    return model

# Register the basic model (writing into our dictionary of models)
register_model_arch("basic", create_basic_model_arch,
                    ["bidir_num_filters", "dense_1_filters", "vocab_size", "embedding_dim", "maxlen", "dropout_rate", "optimizer"])
