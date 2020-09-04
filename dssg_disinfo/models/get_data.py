# Importing necessary packages
import numpy as np
import pandas as pd
import io
import os
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only
from datetime import datetime
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from .model_arch import *

def get_data_and_split(vocab_size, maxlen, model_arch=None, multiple=False, scaler=False):
    '''
    Fetches the data and splits into train/test
    '''
    # Get the paths
    DATA_PATH = os.getenv("DATA_PATH") # we need to change "PATH" to "DATA_PATH" in the ENV File 
    ALL_FEATURES_DATA = os.getenv("ALL_FEATURES_DATA")
    df = pd.read_csv(os.path.join(DATA_PATH, ALL_FEATURES_DATA))
        
    y = df['label'].values # collect target labels
   
    if multiple==True: # True for multiple input model
        
        # Train-test split for two-input model (article text and metadata)
        
        train_nlp_data=df['article_text'].values
        
        train_meta_data = df[['PROPN','ADP','NOUN','PUNCT','SYM',
              'DET','CCONJ','VERB','NUM','ADV',
              'ADJ','AUX','SPACE','X','PRON',
              'PART','INTJ','SCONJ','sent_count','ratio_stops_tokens',
              'len_first_caps','len_all_caps']].values
        
        sentences_train, sentences_test, meta_data_train, meta_data_test, y_train, y_test = train_test_split(
            train_nlp_data, train_meta_data, y, test_size=0.25, random_state = 42)
        
        if scaler==True: # True if the linguistic features need to be scaled
        # scaling metadata features to train data mean/s.d.
            scaler=preprocessing.StandardScaler().fit(meta_data_train)
            scaler.transform(meta_data_train)
            scaler.transform(meta_data_test)
        
        else:
            pass
         
        
    else:     # For basic and word embedding model
        
        sentences = df[['article_pk', 'article_text']]
        
        sentences_train, sentences_test, y_train, y_test = train_test_split(
            sentences, y, test_size=0.25, random_state = 42)
        
        ######## The following code collects the article primary keys of the test data
        file_name = datetime.now().strftime('%Y%m%d%H%M%S')+'.article_pk'
        sentences_test['article_pk'].to_csv(file_name, index=False)
        ######## ----------------------------------------------------------------------
        
        sentences_train = sentences_train['article_text']
        sentences_test = sentences_test['article_text']
        
    # making y into np arrays
    y_train = np.array(y_train)
    y_test = np.array(y_test)
    
    # Tokenize words
    tokenizer = Tokenizer(num_words = vocab_size, oov_token='<OOV>')
    tokenizer.fit_on_texts(sentences_train)
    word_index = tokenizer.word_index
    X_train = tokenizer.texts_to_sequences(sentences_train)
    X_test = tokenizer.texts_to_sequences(sentences_test)

    # Pad sequences with zeros
    X_train = pad_sequences(X_train, padding='post', maxlen=maxlen, truncating='post')
    X_test = pad_sequences(X_test, padding='post', maxlen=maxlen, truncating='post')
    
    if multiple==True:
        return X_train, X_test, meta_data_train, meta_data_test, y_train, y_test
    
    elif model_arch=='word_embedding':
        return X_train, X_test, y_train, y_test, word_index
    
    else:
        return X_train, X_test, y_train, y_test
   
    

        


