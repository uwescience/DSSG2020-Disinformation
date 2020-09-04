import spacy
from spacy.lang.en import English

def get_sent(doc):
    '''
    Extracts sentences demarcated by ( '.', '!', and '?') for each 
    doc object (article text)
    
    Parameters
    ----------
    doc: article text converted to Doc format 
         (a special SpaCy DOC object)
        
    Returns
    -------
    sents: list
        Returns a list of all extracted sentences
    '''
    
    sents = []
    for sent in doc.sents:
        sents.append(sent.text)
    return sents

def extract_sentences(df):
    '''
    Extracts sentences from article text of a given dataframe
    and returns total count of sentences/text
    
    Parameters
    ----------
    df: dataframe
        
    Returns
    -------
    df2: dataframe
        Returns a new dataframe with article_pk, label, 
        total count of sentences/article  and extracted sentences
    '''
    
    nlp = English()  # loads just the language with no model
    sentencizer = nlp.create_pipe("sentencizer") # loads sentencizer 
    nlp.add_pipe(sentencizer)

    df['doc'] = df['article_text'].apply(lambda x: nlp(x))
    df['sentences'] = [get_sent(doc) for doc in df['doc']]
    df['sent_count'] = [len(x) for x in df['sentences']]
    df2 = df[['article_pk', 'label', 'sentences', 'sent_count']].copy()
    return df2