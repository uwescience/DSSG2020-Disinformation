import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only
from keras.preprocessing.text import Tokenizer
from sklearn.model_selection import train_test_split

def write_tokens(input_file, output_file):
    """ Writes tokens after removing \t\n and lowercasing input_file
    
    Parameters
    ----------
    input_file: string, input file location
    output_file: string, output file location
    
    Return
    ------
    None
    
    """
    print("Begin writing tokens.")
    f_in=open(input_file)
    f_in=f_in.read()
    tokenizer = Tokenizer(filters='\t\n',lower=True)
    tokenizer.fit_on_texts([f_in])
    sequences=tokenizer.texts_to_sequences([f_in])
    text=tokenizer.sequences_to_texts(sequences)
    f_out = open(output_file,"w")
    f_out.writelines(text)
    f_out.close()
    print("Writing tokens completed. File: "+output_file)
    return

def return_word_index():
    """ returns word_index from article text
    """
    # Get the paths
    DATA_PATH = os.getenv("DATA_PATH")
    CLEAN_DATA = os.getenv("CLEAN_DATA")
    df = pd.read_csv(os.path.join(DATA_PATH, CLEAN_DATA))

    ### III. Splitting the data into training and testing
    X = df['article_text'] # article_text
    y = df.label

    training_sentences, testing_sentences, training_labels, testing_labels = train_test_split(X, y, random_state = 42)

    # making y into np arrays
    training_labels_final = np.array(training_labels)
    testing_labels_final = np.array(testing_labels)

    vocab_size = 10000 
    embedding_dim = 300
    max_length = 681
    trunc_type='post'
    oov_tok = "<OOV>"


    ### Tokenizing, padding, and truncating
    tokenizer = Tokenizer(num_words = vocab_size, oov_token=oov_tok)
    tokenizer.fit_on_texts(training_sentences)
    word_index = tokenizer.word_index
    return word_index

def return_embedding_matrix(input_file, word_index, embedding_dim=300):
    """ returns embedding matrix of a given file
    
    Parameters
    ----------
    input_file: location of the pretrained vector file
    word_index: word_index of the training data
    embedding_dim: integer, dimension of the embeddings
    
    Return
    ------
    embedding_matrix: numpy array
    """
    
    vocab_size = len(word_index) + 1  # Adding again 1 because of reserved 0 index
    embedding_matrix = np.zeros((vocab_size, embedding_dim))
    #n=0
    with open(input_file) as f_in:
        for line in f_in:
            word = line.split()[0]
            vector = line.split()[-embedding_dim:]
            if word in word_index:
                idx = word_index[word] 
                embedding_matrix[idx] = np.array(vector,
                                                 dtype=np.float32)[:embedding_dim]
    return embedding_matrix
