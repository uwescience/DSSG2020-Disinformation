import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only

def format_date(DATA=None, COLUMN=None):
    ''' Reads in the dataframe with a date column
    Converts the date column into datetime format
    add new column with year
    add new column with month
    add new column with week
    add new column with month and day of the year column
    
    Parameters
    ----------
    None
    
    Returs
    ------
    df: dataframe, with new year, month, week and month_day_year columns
    
    '''
    # Get the paths
    DATA_PATH = os.getenv("DATA_PATH") # Path to the dataframe DATA

    if DATA is None:
        DATA_NAME = os.getenv("CLEAN_DATA")
    else:
        DATA_NAME = DATA
        
    if COLUMN is None:
        COLUMN_NAME = 'publish_date'
    else:
        COLUMN_NAME = COLUMN
        
    df = pd.read_csv(os.path.join(DATA_PATH, DATA_NAME))
    
    #converting date published to datetime data type
    df[[COLUMN_NAME]] = df[[COLUMN_NAME]].apply(pd.to_datetime)
    
    # extracting time from datetime and changing format to m-d-y
    df['year'] = df[COLUMN_NAME].dt.to_period('Y')
    df['month'] = df[COLUMN_NAME].dt.to_period('M')
    df['week'] = df[COLUMN_NAME].dt.to_period('W')
    df['month_day_year'] = df[COLUMN_NAME].dt.to_period('D').dt.strftime('%m-%d-%Y')
    
    return df
    
    
    
    
    
    
