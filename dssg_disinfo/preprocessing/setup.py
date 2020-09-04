from dotenv import load_dotenv
from langdetect import detect
from pathlib import Path  # Python 3.6+ only
import pandas as pd
import numpy as np
import spacy
import os

# Path to the environment variables file .env
env_path = '.env'
load_dotenv(env_path, override=True)

def replace_char(DATA, CHAR, COLUMN=None):
    """ Replace various whitespace characters with single space
    
    Parameters
    ----------
    DATA: dataframe
    CHAR: charcter that needs to be replaced
    COLUMN: column from which the character has to be replaced
    
    Returns
    -------
    None
    """
    if COLUMN is None:
        COLUMN_NAME='article_text'
    else:
        COLUMN_NAME=COLUMN
    
    DATA[COLUMN_NAME]=[str(column).replace(CHAR, ' ') for column in DATA[COLUMN_NAME]]
    return


def remove_non_ascii(DATA, COLUMN=None):
    """ Remove all non-ASCII characters
    
    Parameters
    ----------
    DATA: dataframe
    COLUMN: column from which non-ASCII charcters will be removed
    
    Return
    ------
    None
    """
    if COLUMN is None:
        COLUMN_NAME='article_text'
    else:
        COLUMN_NAME=COLUMN
        
    DATA[COLUMN_NAME] = [str(column).encode('ascii', errors='ignore').decode() for column in DATA[COLUMN_NAME]]
    return 

def find_url(text):
    '''
    Parameter
    ---------
    text: the text in which URL needs to be found
    
    Return
    ------
    list: All URLS embedded in the input text
    '''
    urls = (re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text))
    
    return urls


def load_GDIdata():
    ''' This function will load the two data sets (negative and positive) and concatenate them to produce
    a single data frame.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    df: dataframe, concatenated dataframe
    '''
    DATA_PATH = os.getenv("DATA_PATH") # Path to the dataframe DATA
    NEGATIVE_DATA = os.getenv("NEGATIVE_DATA")
    POSITIVE_DATA = os.getenv("POSITIVE_DATA")
    df_neg = pd.read_csv(os.path.join(DATA_PATH,NEGATIVE_DATA)) # Load negative data
    df_pos = pd.read_csv(os.path.join(DATA_PATH,POSITIVE_DATA)) # Load positive data
    df = pd.concat([df_pos, df_neg], ignore_index=True) # Concatanate negative and positive articles
    return df


def clean_data(DATA=None):
    """ Cleans the DATA and performs the following steps:
    Drops empty article_text rows
    Removes duplicate article_text
    Remove non-english article_text from the dataframe
    Remove noisy characters from article_text
    Converting all characters in article_text to ascii- removes emoticons
    Exports clean data in CLEAN_DATA named dataframe in DATA_PATH location
    
    Parameters
    ----------
    DATA: dataframe, which needs to be cleaned
    
    Returns
    -------
    None
    """
    DATA_PATH = os.getenv("DATA_PATH") # Path to the dataframe DATA
    CLEAN_DATA = os.getenv("CLEAN_DATA") # Path where clean dataframe will be written
    if DATA is None:
        df=load_GDIdata()
    else:
        df = DATA
    
    print("Removing empty rows from articles")
    # Drop empty article_text rows
    df.dropna(subset=['article_text'], inplace=True)
    
    print("Dropping duplicate articles")
    # Drop duplicated article_text
    df.drop_duplicates(subset='article_text', keep='first', inplace=True)
    
    print("Removing non-english articles")
    # Index of non-english rows
    non_en_index = []
    for index, row in df.iterrows():
        # Explicitly converting article_text to string because a few of the rows were being captured as non-strings
        lang = detect(str(row['article_text']))
        if lang != 'en':
            non_en_index.append(index)

    # Removing non-english articles        
    df.drop(non_en_index, inplace=True)
    
    print("Removing whitespace characters")
    nonspace_ws_characters = ['\n', '\t', '\r', '\v', '\f'] # List of variout white space characters
    
    for char in nonspace_ws_characters:  
        replace_char(df, char, 'article_text')
                         
    print("Replacing urls with token EMBD_HTML")                     
    # Encoding URLs
    pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+' # regex for https urls
    df['article_text'].replace(to_replace = pattern, value = 'EMBD_HTML', regex=True, inplace=True)
    
    pattern = r'[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)' # regex for urls without https
    df['article_text'].replace(to_replace=pattern, value='EMBD_HTML', regex=True, inplace=True)
    
    print("Removing non-ASCII characters")
    # Removing non-ASCII characters                     
    remove_non_ascii(df, 'article_text')
    
    print("Exporting clean data")
    # Export clean data
    df.to_csv(os.path.join(DATA_PATH, CLEAN_DATA), index=False)

    return
