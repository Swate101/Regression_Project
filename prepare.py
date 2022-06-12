import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

from env import get_db_url
from sklearn.model_selection import train_test_split

import sklearn.preprocessing

# Joseph Goerner
# ------------------------------------------------------------------------------------- PREPARE---------------------------------

#Clean the Zillow data

def clean_zillow(df):
    '''
    Takes in a df of zillow data acquired from sql_query
    and cleans the data appropriately by:
    - handling null values by dropping and imputing
    - converting float variables that do not require a decimal to ints
    - dropping outliers
    - changing columns names
    - drop columns
    - adding new columns
    - scaling data
    return: df, a cleaned pandas dataframe
    '''
    #droping buildingqualitytypeid until I figure out best method to use it 
    df.drop(['buildingqualitytypeid'], axis=1, inplace=True)
    #DROPING NULLS
    df = df.dropna()
    #add two new columns for my method of use 
    df['property_age'] = 2021 - df.yearbuilt
    df['tax_rate'] = (df.taxamount / df.taxvaluedollarcnt)
    #change data types from float to int as required by the model and the designated plan 
    df['bedroomcnt'] = df.bedroomcnt.astype('int')
    df['yearbuilt'] = df.yearbuilt.astype('int')
    df['regionidzip'] = df.regionidzip.astype('int')
    df['regionidcounty'] = df.regionidcounty.astype('int')
    df['fips'] = df.fips.astype('int')
    df['latitude'] = df.latitude.astype('int')
    df['longitude'] = df.longitude.astype('int')
    df['property_age'] = df.property_age.astype('int')
    df = df.set_index("parcelid")
    #rename columns for ease of access and use 
    df = df.rename(columns={"bedroomcnt": "bedrooms", 
                            "bathroomcnt": "bathrooms", 
                            "calculatedfinishedsquarefeet": "square_feet", 
                            "taxvaluedollarcnt": "tax_value",
                            "regionidzip": "zip_code",
                            "regionidcounty": "county"})

    return df

#generic split that I have learned in class -------------------------------
def split_data(df):
    '''
    split the data,
    takes in a pandas dataframe
    returns: three pandas dataframes, train, test, and validate
    '''
    train_val, test = train_test_split(df, train_size=0.8, random_state=123)
    train, validate = train_test_split(train_val, train_size=0.7, random_state=123)
    return train, validate, test

#split with -----------------------------
def train_validate_test_split(df, target, seed):
    '''
    spilts the data  into train, validate, test
    by taking in a dataframe and dividing into
    separate
    '''
    # Train, Validate, and test
    train_and_validate, test = train_test_split(
        df, test_size=0.2, random_state=seed)
    train, validate = train_test_split(
        train_and_validate,
        test_size=0.3,
        random_state=seed)
    
    # Split with X and y
    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    X_test = test.drop(columns=[target])
    y_test = test[target]
    
    return train, validate, test, X_train, y_train, X_validate, y_validate, X_test, y_test   
