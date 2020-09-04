# Lexical features

import pandas as pd
import re as re
import nltk as nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
nltk.download('stopwords')

def token_features(dataframe, article_id_var, input_text_var):
    """
        input: (1) dataframe, (2) the unique identifier variable, and (3) text from a particular column in dataframe
        
        returns: new dataframe with following new columns:
            -tokenized: tokenized list of words from input text (input_text_var)
            -len_tokens: number of tokens in each text cell
            -stopwords: tokenized list of stopwords in each text cell
            -len_stopwords: number of stopwords in each text cell
            -ratio_stops_tokens: ratio of number of stopwords/number of total words in each text cell
            -first_caps: list of all words with the first letter Capitalized in each text cell
            -len_first_caps: number of words with the first letter Capitalized in each text cell
            -all_caps: list of all words with all letters CAPITALIZED in each text cell
            -len_all_caps: number of words with all letters CAPITALIZED in each text cell
            -avg_len_characters: average character length of words in each text cell
            
    """
    # Create new dataframe with "article_pk" idenitifier
    new_df = pd.DataFrame(dataframe[article_id_var])
    
    # Define tokenizer and tokenize text input
    tokenizer = RegexpTokenizer(r'\w+')
    new_df['tokenized'] = dataframe.apply(lambda row: tokenizer.tokenize(str(row[input_text_var])), axis=1)
    # Calculate the word length of each article
    new_df['len_tokens'] = new_df['tokenized'].apply(lambda x: len(x))
    
    # Calculate the ratio of stop words to total words
    stopwords_english = stopwords.words('english')
    new_df['stopwords'] = new_df.apply(lambda row: [token for token in row['tokenized'] 
                                                    if token in stopwords_english], axis=1)
    new_df['len_stopwords'] = new_df['stopwords'].apply(lambda x: len(x))
    new_df['ratio_stops_tokens']= new_df['len_stopwords']/new_df['len_tokens']

    # Find words that have first letter capitalized and put in new column
    new_df['first_caps'] = new_df.apply(lambda row: re.findall('([A-Z][a-z]+)', str(row['tokenized'])), axis=1)
    new_df['len_first_caps'] = new_df['first_caps'].apply(lambda x: len(x))
    # Find words that are in all capitals and put in new column
    new_df['all_caps'] = new_df.apply(lambda row: re.findall('([A-Z][A-Z]+)', str(row['tokenized'])), axis=1)
    new_df['len_all_caps'] = new_df['all_caps'].apply(lambda x: len(x))
    
    # Find unique tokens and put in new column
    new_df['unique_toks'] = new_df.apply(lambda row: set(row['tokenized']), axis=1)
    new_df['len_unique'] = new_df['unique_toks'].apply(lambda x: len(x))
    
    # Average size of words (in characters)
    new_df['avg_len_characters'] = new_df.apply(lambda row: sum([len(token) for token in row['tokenized']])/len(row['tokenized']), axis=1)

    return new_df