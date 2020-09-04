import re
import pandas as pd

def find_url(text):
    '''Finds URLS embedded in a text and extracts them as a list
    
    Parameters
    ----------
    str: 
        text
        
    Returns
    -------
    urls: list
          

    Returns a list of all URLS embedded in a text 
    
    '''
    
    urls = []
    urls = (re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text))
    return urls

    
def url_list(all_data):
    '''Identifies urls in each article text and creates a new column with 
    the list of identified urls as well as 
    
    Parameters
    ----------
    object: 
        all_data datarame
        
    Returns
    -------
    None

    '''
    all_data['urls'] = [find_url(cell) for cell in all_data['article_text']]
    return 


def url_len(all_data): 
    '''Counts embedded urls for a given article and records the number in a new column
    
    Parameters
    ----------
    object: 
        all_data dataframe
        
    Returns
    -------
    None 
    
    '''
    all_data['no_urls'] = [len(x) for x in all_data['urls']]
    return 

def process_urls(all_data):
    '''Finds and counts all URLS in a text saving results to 
    separate columns
    
    Parameters
    ----------
    object:
        all_data dataframe
        
    Returns
    -------
    object:
        dataframe with two new columns: count of urls in article text,
        list of all extracted urls
    
    '''
    url_list(all_data)
    url_len(all_data)
    return all_data

