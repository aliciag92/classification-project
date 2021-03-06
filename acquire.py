import pandas as pd
import numpy as numpy
from env import host, user, password 

#defines function to create a sql url using personal credentials
def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

#returns telco data from MySQL as a pandas DataFrame
def get_telco_data():
    '''
    This function reads in the telco_churn data from the Codeup db,
    joins contract-, internet-service-, and payment-types tables, 
    and returns a pandas DataFrame with all columns.
    '''
    #create SQL query
    sql_query = '''
                SELECT * FROM customers
                JOIN contract_types USING(contract_type_id)
                JOIN internet_service_types USING(internet_service_type_id)
                JOIN payment_types USING(payment_type_id)
                '''
    
    #read in dataframe from Codeup db
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    
    return df