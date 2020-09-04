import spacy
from spacy.lang.en import English
from collections import Counter
import pandas as pd
from joblib import Parallel, delayed

nlp = spacy.load('en_core_web_sm')

#Tagging parts of speech
def pos_pipe(doc):
    ''' Tags each word in a given text with part-of-speech(POS) tag and
    returns a list for each text of extracted tags
    
    Parameters
    ----------
    doc: article text converted to Doc format 
        A special SpaCy DOC object 
        
    Returns
    -------
    pos_list: list
        Returns a list of all pos taggs in a text 
    '''
    
    pos_list = [tok.pos_ for tok in doc] 
    return pos_list

def chunker(iterable, total_length, chunksize):
    ''' Parses the conversion process 
    
    Parameters
    ----------
    iterable: in this case text 
    total_length: the length of dataframe (rows)
    chunksize: how many rows are in a chunk
        
    Returns
    -------
    just the process
    '''
    return (iterable[pos: pos + chunksize] for pos in range(0, total_length, chunksize))

def flatten(list_of_lists):
    ''' Flattens a list of lists to a combined list
    
    Parameters
    ----------
    list_of_lists:
        this is a list 
        
    Returns
    -------
    flattened list
    '''
    return [item for sublist in list_of_lists for item in sublist]

def process_chunk(texts):
    ''' Applies the preprocess pipe to article text
    and returns it
    
    Parameters
    ----------
    texts: article text 
        
    Returns
    -------
    preproc_pipe: list
        Returns a list of POS tags
    '''
    preproc_pipe = []
    for doc in nlp.pipe(texts, batch_size=20):
        preproc_pipe.append(pos_pipe(doc))
    return preproc_pipe

def preprocess_parallel(texts, df, chunksize=100):
    ''' Processes article text with NLP SpaCy
    and returns a all pos tags for a text
    
    Parameters
    ----------
    texts: article text 
    chunksize: # of chunks for processing
        
    Returns
    -------
    preproc_pipe: list
        Returns a list of POS tags
    '''
    
    executor = Parallel(n_jobs=7, backend='multiprocessing', prefer="processes")
    do = delayed(process_chunk)
    tasks = (do(chunk) for chunk in chunker(texts, len(df), chunksize=chunksize))
    result = executor(tasks)
    return flatten(result)

def tag_pos(df):
    ''' Tags each word in a given text with part-of-speech(POS) tag and 
    returns pos frequency for each text in dataframe
    
    Parameters
    ----------
    df: Dataframe
        Dataframe with a text column that needs to be tagged for parts-of-speech
        
    Returns
    -------
    Dataframe
        Returns a new dataframe
    POS TAG Scheme 
    POS	   Description	     Examples
    ADJ	   adjective	     big, old, green, incomprehensible, first
    ADP	   adposition	     in, to, during
    ADV	   adverb	         very, tomorrow, down, where, there
    AUX	   auxiliary	     is, has (done), will (do), should (do)
    CONJ   conjunction       and, or, but
    CCONJ  coordinating      and, or, but
           conjunction	
    DET	   determiner	     a, an, the
    INTJ   interjection      psst, ouch, bravo, hello
    NOUN   noun	             girl, cat, tree, air, beauty
    NUM	   numeral	         1, 2017, one, seventy-seven, IV, MMXIV
    PART   particle	         ’s, not,
    PRON   pronoun	         I, you, he, she, myself, themselves, somebody
    PROPN  proper noun       Mary, John, London, NATO, HBO
    PUNCT  punctuation	     ., (, ), ?
    SCONJ  subordinating     if, while, that
           conjunction	
    SYM	   symbol	        $, %, §, ©, +, −, ×, ÷, =, :), 😝
    VERB   verb	            run, runs, running, eat, ate, eating
    X	   other	        sfpksdpsxmsa
    SPACE  space	    
    '''
    
    nlp = spacy.load('en_core_web_sm')
    df['preproc_parallel'] = preprocess_parallel(df['article_text'], df, chunksize=1000)
    df['Count'] = [Counter(l) for l in df['preproc_parallel']]
    df2 = pd.concat([df.drop(columns=['Count', 'article_text', 'preproc_parallel', 'domain_pk', 'domain_name',
                                     'article_url']),df['Count'].apply(pd.Series)], axis=1)
    df2.fillna(value=0, inplace=True)
    return df2 