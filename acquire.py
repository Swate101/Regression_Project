import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

from env import get_db_url
from sklearn.model_selection import train_test_split

import sklearn.preprocessing

# Joseph Goerner
#Connection function to access Codeup Database and retrieve zillow dataset from mysql


#------------------------------------------------------------------------------------ACQUIRE--------------------------------------------------

#This function reads in the zillow data from the Codeup 
    #Database connection made from get_connection
    #and returns a pandas DataFrame with all columns in tow, needed to start this proccess


def acquire_zillow():
    '''
    This function reads in the zillow data from the Codeup 
    Database connection made from get_connection
    and returns a pandas DataFrame with all columns in tow, needed to start this proccess
    '''
    sql_query = '''
                SELECT parcelid, bedroomcnt, bathroomcnt, buildingqualitytypeid, yearbuilt, 
                regionidcounty, regionidzip, fips, latitude, longitude, calculatedfinishedsquarefeet, 
                taxamount, taxvaluedollarcnt
                FROM  properties_2017
                JOIN predictions_2017 USING(parcelid)
                WHERE transactiondate between "2017-05-01" and "2017-08-31"
                and unitcnt = 261 or 263 or 273 or 274 or 276 or 279;
                '''

    
    return pd.read_sql(sql_query, get_db_url('zillow'))    

# This function reads in zillow data from Codeup database and 
    #writes data to a csv file if cached == False. If cached == True 
    #reads in zillow df from a csv file, returns df. 


def get_zillow_data(cached=False):
    '''
    This function reads in zillow data from Codeup database and 
    writes data to a csv file if cached == False. If cached == True 
    reads in zillow df from a csv file, returns df. 
    '''
    if cached == False or os.path.isfile('zillow.csv') == False:
        
        # reads the infomation from the data frame and database
        df = acquire_zillow()
        
        # Write DataFrame to a csv file.
        df.to_csv('zillow.csv')
        
    else:
        
        # I have  found that the notebook once the cvs is imported will keep reverting to same file 
        df = pd.read_csv('zillow.csv', index_col=0)
        
    return df
