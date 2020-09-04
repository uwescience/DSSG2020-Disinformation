import numpy as np
import pandas as pd
import io
import os
from pathlib import Path  # Python 3.6+ only
from datetime import datetime
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers.embeddings import Embedding
from tensorflow.keras.callbacks import CSVLogger
from keras.wrappers.scikit_learn import KerasClassifier
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import (RandomizedSearchCV,
                                     StratifiedKFold, 
                                     train_test_split)
import joblib
import pickle
from tensorflow.keras import layers
from keras.models import Sequential
from keras.layers import (Dense,
                          LSTM,
                          Bidirectional,
                          Dropout)
import matplotlib.pyplot as plt
from .word_embedding_arch import *
from .get_data import *
from .baseline_model import create_basic_model_arch

def param_tune(model_arch, **copacabana):
    '''Runs parameter tuning.
    input
    -----
    model_arch: string, specifies which model to run
    **copacabana: variable length of parameters
    
    output
    ------
    file_name: string, log file for best model fit
    '''
    
    # Storing all the parameters into copacabana, parameters passed by user will overwrite default
    copacabana = {k: copacabana.get(k, copacabana[k]) for k in copacabana.keys()}
    
    #Parameter grid for grid search
    param_grid = dict(bidir_num_filters=[32, 64, 128],
                      dense_1_filters=[10],
                      vocab_size=[10000],
                      embedding_dim=[100, 200, 300],
                      maxlen=[681],
                      dropout_rate=[0.2, 0.3, 0.4],
                      optimizer=['adam', 'nadam'])
    
    # File to save the model logs
    file_name = datetime.now().strftime('%Y%m%d%H%M%S') +'_'+model_arch+'.log'
    csv_logger = CSVLogger(file_name, append=True, separator=';')
    
    if model_arch == 'basic':
        model_new = KerasClassifier(build_fn = create_basic_model_arch) # baseline_model.py function
        grid = RandomizedSearchCV(estimator=model_new,
                                  param_distributions=param_grid,
                                  cv = StratifiedKFold(n_splits=2),
                                  verbose=0,
                                  n_iter=10,
                                  scoring='accuracy')
        
        print("Loading data.")
        #pull in data
        X_train, X_test, y_train, y_test = get_data_and_split(copacabana['vocab_size'],
                                                              copacabana['maxlen']) # get_data.py function

        
        grid.fit(X_train, y_train,
                epochs=copacabana['epochs'])
        
        print("Best model parameters are:")
        print(grid.best_params_)
        
        print("Fitting the best model with data.")
        
        grid.best_estimator_.fit(X_train,
                                 y_train,
                                 epochs=copacabana['epochs'],
                                 validation_data=(X_test, y_test),
                                 callbacks=[csv_logger])
        
        print("Saving the model")
        grid.best_estimator_.model.save('best_model.h5')
        
        print(f"Fitting completed. Refer {file_name}.")
        
        ### the following code saves the predictions into a file for future analysis
        predictions_file_name = datetime.now().strftime('%Y%m%d%H%M%S')+'_'+model_arch+'.predict'
        
        df1=pd.DataFrame(y_test)
        pred=grid.predict(X_test)
        df2=pd.DataFrame(pred)
        df_new=pd.concat([df1, df2],keys=['label','predicted_label'], axis=1)
        df_new.to_csv(predictions_file_name, sep=',',index=False )
        ################ -----------------------------------------------------------
        
        return file_name
    
    elif model_arch == 'multiple':
        return None
        
    elif model_arch == 'word_embedding':
        
        model_new = KerasClassifier(build_fn = create_word_embd_model_arch) # updated this for embd

        grid = RandomizedSearchCV(estimator=model_new,
                                  param_distributions=param_grid,
                                  cv = StratifiedKFold(n_splits=5),
                                  verbose=0,
                                  n_iter=1,
                                  scoring='accuracy')
        
        print("Loading data.")
        #pull in data
        X_train, X_test, y_train, y_test = get_data_and_split(copacabana['vocab_size'],
                                                              copacabana['maxlen'])

        grid.fit(X_train, y_train,
                 epochs=copacabana['epochs'],
                 validation_data=(X_test, y_test))
                
        print("Best model parameters are:")
        print(grid.best_params_)
        
        print("Fitting the best model with data.")
        
        grid.best_estimator_.fit(X_train,
                                 y_train,
                                 epochs=copacabana['epochs'],
                                 validation_data=(X_test, y_test),
                                 callbacks=[csv_logger])
        
        print("Saving the model")
        grid.best_estimator_.model.save('best_model.h5')
        
        print(f"Fitting completed. Refer {file_name}.")
        
        ### the following code saves the predictions into a file for future analysis
        predictions_file_name = datetime.now().strftime('%Y%m%d%H%M%S')+'_'+model_arch+'.predict'
        
        df1=pd.DataFrame(y_test)
        pred=grid.predict(X_test)
        df2=pd.DataFrame(pred)
        df_new=pd.concat([df1, df2],keys=['label','predicted_label'], axis=1)
        df_new.to_csv(predictions_file_name, sep=',',index=False )
        ################
        return file_name
    
    else:
        return None