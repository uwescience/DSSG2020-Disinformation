from nltk.tokenize import sent_tokenize, word_tokenize
import gensim
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors


def w2v_embedding(input_file, bin_file, output_file):
    """ This function converts words in a text file into word embeddings using word2vec.
    The default dimension of the word embedding is 200.
    
    Parameters
    ----------
    input_file: string, input file location
    bin_file: string, bin file location
    output_file: string, output file location
    
    Returns
    -------
    None
    """
    print("Loading the training corpus.")
    df = open(src_file_path, "r") # Open the text file stored at src_file_path
    df = df.read()    # Read the text file
    tokens1 = word_tokenize(df) # Tokenize
    token_list = []
    print("Writing the bin file.")
    models = KeyedVectors.load_word2vec_format(bin_destination_file_path, binary=True) # Save bin format
    print("Saving the word embeddings.")
    models.save_word2vec_format(txt_file_destination_path, binary=False) # Save the word vectors
    
    return txt_file_destination_path