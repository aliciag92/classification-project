import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

########################### Clean Telco Data ############################

def clean_telco(df):
    '''
    clean_telco will take one argument df, a pandas dataframe and will:
    set customer_id as the first column,
    shorten column names
    encode yes/no/no ___ columns
    fill in missing values
    replace missing values from total_charges and convert to float
    create dummy variable for gender, rename dummy column, and add to original df
    adjust values
    drop redundant columns
    set floats to integers (except monthly/total charges)
    
    return: a single pandas dataframe with the above operations performed
    '''
    #set customer_id as first column
    df = df.set_index('customer_id')
    
    
    #shorter column names: 
    df = df.rename(columns={"payment_type_id": "payment_type", 
                            "internet_service_type_id": "internet_type",
                            "contract_type_id": "contract",
                            "senior_citizen": "senior", 
                            "phone_service": "phone", 
                            #set up payment_type column for encoding:
                            "payment_type": "auto_pay"})
    
    
    #yes/no columns only
    df.partner = df.partner.map({'No': 0, 'Yes': 1})
    df.dependents = df.dependents.map({'No': 0, 'Yes': 1})
    df.phone = df.phone.map({'No': 0, 'Yes': 1})
    df.paperless_billing = df.paperless_billing.map({'No': 0, 'Yes': 1})
    df.churn = df.churn.map({'No': 0, 'Yes': 1})


    #yes/no/no___ columns (replace "no ___ service" with "no" before encoding)
    df.multiple_lines = df.multiple_lines.replace('No Phone Service', 'No')
    df.multiple_lines = df.multiple_lines.map({'No': 0, 'Yes': 1})

    df.online_security = df.online_security.replace('No internet Service', 'No')
    df.online_security = df.online_security.map({'No': 0, 'Yes': 1})

    df.online_backup = df.online_backup.replace('No internet Service', 'No')
    df.online_backup = df.online_backup.map({'No': 0, 'Yes': 1})

    df.device_protection = df.device_protection.replace('No internet service', 'No')
    df.device_protection = df.device_protection.map({'No': 0, 'Yes': 1})

    df.tech_support = df.tech_support.replace('No internet service', 'No')
    df.tech_support = df.tech_support.map({'No': 0, 'Yes': 1})

    df.streaming_tv = df.streaming_tv.replace('No internet service', 'No')
    df.streaming_tv = df.streaming_tv.map({'No': 0, 'Yes': 1})

    df.streaming_movies = df.streaming_movies.replace('No internet service', 'No')
    df.streaming_movies = df.streaming_movies.map({'No': 0, 'Yes': 1})
    
    #fill missing numbers
    df = df.fillna(0)
    
    #replace total_charges missing values and convert to float
    df.total_charges = df.total_charges.str.replace(' ', '0').astype(float)
    
    
    #create dummy variable for gender, rename dummy column, and add to original df
    dummies = pd.get_dummies(df[['gender']], drop_first=True)
    dummies.rename(columns={'gender_Male': 'gender_male'}, inplace=True)
    df = pd.concat([df,dummies], axis=1)

    
    #adjust values
    df.contract_type = df.contract_type.replace({'Month-to-month': 0, 
                                                 'One year': 1, 
                                                 'Two year': 2})

    df.internet_service_type = df.internet_service_type.replace({'None': 0, 
                                                                 'DSL': 1, 
                                                                 'Fiber optic': 2})

    df.auto_pay = df.auto_pay.replace({'Electronic check': 0, 
                                       'Mailed check': 0, 
                                       'Bank transfer (automatic)': 1, 
                                       'Credit card (automatic)': 1})


    #drop redundant columns
    df = df.drop(columns=['payment_type', 'internet_type', 'contract', 'gender'])


    #set floats to integers
    df.multiple_lines = df.multiple_lines.astype('int')
    df.online_security = df.online_security.astype('int')
    df.online_backup = df.online_backup.astype('int')
    

    return df




########################### Generic Split Function ############################


def split(df, stratify_by=None):
    """
    Crude train, validate, test split
    To stratify, send in a column name
    """
    
    if stratify_by == None:
        train, test = train_test_split(df, test_size=.2, random_state=123)
        train, validate = train_test_split(train, test_size=.3, random_state=123)
    else:
        train, test = train_test_split(df, test_size=.2, random_state=123, stratify=df[stratify_by])
        train, validate = train_test_split(train, test_size=.3, random_state=123, stratify=train[stratify_by])
    
    return train, validate, test