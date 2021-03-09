# Predicting customer churn at Telco
****

## About the Project

****

The Codeup Data Science Team wants to understand why customers at Telco, a telecommunications company, are churning. Objectives for this project include: 
- Identifying the features to understand why customers are leaving the company.
- Finding the drivers for customer churn.
- Documenting process and analysis throughout the data science pipeline.
- Constructing a Machine Learning classification model that predicts future customer churn as accurately as possible.
- Deliverables:
    - README.md file containing overall project information.
    - [Jupyter Notebook Report](https://github.com/aliciag92/classification-project/blob/main/telco-churn-report.ipynb) detailing the process to create model and predictions.
    - Individual modules for [data acquisition](https://github.com/aliciag92/classification-project/blob/main/acquire.py) and [data preparation](https://github.com/aliciag92/classification-project/blob/main/prepare.py) that house functions to acquire and prepare data.
    - Final [CSV file](https://github.com/aliciag92/classification-project/blob/main/predictions.csv) with customer_id, probability of churn, and prediction of churn.
    - Notebook walkthrough

****
## Data Dictionary
    
| **Feature**          | **Definition**                                        | **Data Type**  |
|----------------------|-------------------------------------------------------|----------------|
| senior               | senior or not                                         | int - boolean  |
| partner              | has partner or not                                    | int - boolean  |
| dependents           | has dependents or not                                 | int - boolean  |   
| phone                | has phone or not                                      | int - boolean  |  
| multiple_lines       | has multiple lines or not                             | int - boolean  |  
| paperless_billing    | has paperless billing or not                          | int - boolean  |
| churn                | customer left or not                                  | int - boolean  |
| contract_type        | monthly, 1 year, 2 year                               | int - (0-2)    |
| internet_service_type| none, DSL, fiber optic                                | int - (0-2)    |
| auto_pay             | auto pay or not                                       | int - boolean  |
| gender_male          | binary M/F                                            | int - boolean, dummy var of gender |
| streaming_services   | none, tv or movies, both                              | int - (0-2)    |
| add_ons              | none, online security/backup, device protection, tech support| int - (0-4) |



****


## Project Process Overview
#### 1. Plan
#### 2. Acquire
#### 3. Prepare
#### 4. Explore
#### 5. Model/Evaluate
#### 6. Deliver

****

## Recreate Project
- [Telco Churn Report](https://github.com/aliciag92/classification-project/blob/main/telco-churn-report.ipynb)

****
## Key Findings
- Customers most likely to churn:
    - Seniors
    - Month-to-month contracts
    - Add_ons
- The model is able to correctly predict 77% of customers who actually churn.
- Model based on features are good predictors of churn. 

****

## Recommendations
- Apply a first month discount
- Special for add-ons
- Senior discount 