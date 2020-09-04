from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only
import pandas as pd
import numpy as np
import spacy
import os

def pre_trained_glove_word_embedding(DATA=None, COLUMN=None):
    """ Pretrained glove vectorisation of input column using SpaCy
    
    Parameters
    ----------
        DATA: dataframe
        COLUMN: column to be vectorised
    
    Returns
    -------
        df_vector: numpy array of the glove vectors of the column
    """
    
    DATA_PATH = os.getenv("DATA_PATH") # Path to the dataframe DATA
    if DATA is None:
        DATA_NAME = os.getenv("CLEAN_DATA")
    else:
        DATA_NAME = DATA
        
    if COLUMN is None:
        COLUMN_NAME = 'article_text'
    else:
        COLUMN_NAME = COLUMN
        
    df = pd.read_csv(os.path.join(DATA_PATH,DATA_NAME)) # Load DATA_NAME from PATH
    
    nlp = spacy.load('en_vectors_web_lg') # Load the english vectors from spacy
    
    print("Vectorising begins. Please wait.")
    df_vector = np.asarray([nlp(column).vector for column in df[COLUMN_NAME]]) # Convert text column into a vector numpy array
    print("Vectorising complete. Returning the array.")

    return df_vector