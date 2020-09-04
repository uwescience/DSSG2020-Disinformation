# Importing necessary packages
import numpy as np
import pandas as pd
import io
import os
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only

from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers.embeddings import Embedding
from tensorflow.keras.callbacks import CSVLogger
from tensorflow.keras import layers
from sklearn.metrics import roc_curve, auc
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Flatten, LSTM, Bidirectional, Conv1D, MaxPooling1D, Dropout, Activation
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


_model_arch_registry = {}

def register_model_arch(arch_name, create_fn, param_names):
    '''
    register_model_arch(arch_name, create_fn, param_names) registers a model architecture
    with the given name so that it can be built with the build_model() function.
    
    Inputs:
    arch_name: should be a string that identifies the model.
    create_fn: should be a function that accepts the parameters in the param_names and
        yields a sequential model.
    param_names: should be a list of the names of the parameters that create_fn() requires.
    
    Returns:
    none but does register the model create_fun() and param_names (parameters required for this function
    in the model registry under the model's name.
    '''
    # Save the model
    _model_arch_registry[arch_name] = (create_fn, param_names)

def build_model_arch(arch_name, param_dict):
    '''
    build_model_arch(arch_name, param_dict) pulls the model details for the given model
    from the model registry so that it can be built with the build_model() function.
    
    Inputs:
    arch_name: should be a string that identifies the model.
    param_dict: a list of parameters that are necessary to run the model.
    
    Returns:
    create function for given model and set of parameters.
    '''
    
    # lookup the params and create function:
    (create_fn, params) = _model_arch_registry[arch_name]
    # The f(*[...]) syntax means that instead of being called as f([a,b,c]) the
    # functiion call is converted into f(a, b, c).
    return create_fn(*[param_dict[k] for k in params])


        
        
