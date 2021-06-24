# Burn the Telco Churn
****
![burnchurn](https://growtraffic-bc85.kxcdn.com/blog/wp-content/uploads/2015/11/Churn-and-Burn-Website.jpg)
## About the Project

****

The Codeup Data Science Team wants to understand why customers at Telco, a telecommunications company, are churning. The churn rate, also known as the rate of attrition or customer churn, is the rate at which customers stop doing business with an entity. 

### Objectives for this project include: 
- Identifying the features to understand why customers are leaving the company.
- Finding the drivers for customer churn.
- Documenting process and analysis throughout the data science pipeline.
- Constructing a Machine Learning classification model that predicts future customer churn as accurately as possible.
- Deliverables:
    - README.md file containing overall project information.
    - [Jupyter Notebook Report](https://github.com/aliciag92/classification-project/blob/main/telco-churn-report.ipynb) detailing the process to create model and predictions.
    - Individual modules for [data acquisition](https://github.com/aliciag92/classification-project/blob/main/acquire.py) and [data preparation](https://github.com/aliciag92/classification-project/blob/main/prepare.py) that house functions to acquire and prepare data.
    - Final [CSV file](https://github.com/aliciag92/classification-project/blob/main/predictions.csv) with customer_id, probability of churn, and prediction of churn.
    - Notebook walkthrough.

### Initial Hypotheses
- Are senior citizens more likely to churn than non-senior citizens?
- Is there a difference in the rate of churn for customers who have streaming services vs customers who do not?
- Does contract type play a role in churn rate?
- Do customers with add-on's churn more that customers without any add-on's?

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


## Pipeline Process: 

### Plan
- Understand project description and goals.
- Form hypotheses and brainstorm ideas.
- Have all necessary imports ready for project.

### Acquire
- Define functions to:
    - create a sql url using personal credentials.
    - get telco data from MySQL and return as a pandas DataFrame.
- Functions to acquire the data are included in [acquire.py](https://github.com/aliciag92/classification-project/blob/main/acquire.py).
- Bring in acquired data frame into notebook using custom functions from .py file.
- Complete initial data summarization and plot distributions of individual variables to get to know data and know what is needed to be prepped/cleaned.

### Prepare
- Define functions to:
    - clean telco data and return as a cleaned pandas DataFrame.
    - split the dataframe into train, validate, test
- Functions to prepare/split the data are included in [prepare.py](https://github.com/aliciag92/classification-project/blob/main/prepare.py)
- Bring in cleaned data frame into notebook and split the data using custom functions from .py file.

### Explore
- Address questions posed in planning and brainstorming and figure out drivers of customer churn.
- Create visualizations and run statistical tests (as many as needed).
- Summarize key findings and takeaways.

### Model/Evaluate
- Establish and evaluate a baseline model. 
- Generate various classification algorithms with varying hyperparameters (as many as needed) and settle on the best algorithm by comparing evaluation metrics.
- Choose the best model and test that final model on out-of-sample data.
- Summarize performance, interpret, and document results.

### Deliver
- K-Nearest Neighbor model with specified parameters (n_neighbors = 20) and specified features (senior, streaming_services, contract_type, add_ons) beat the baseline by 4%.
    - 76% accuracy on training data
    - 77% accuracy on validate data 
    - 77% accuracy on test data
- This model based on the parameters and features specified is able to correctly predict 77% of customers who actually churn. 
- It should be used to come up with ways to improve contract types, add ons and/or appeal more to seniors, people with streaming services.
- CSV file with predictions and probability of customer churn can be found [here](https://github.com/aliciag92/classification-project/blob/main/predictions.csv).
****

## Recommendations
- Apply a first month discount.
- Create special discounts for add-on features.
- Give senior discounts.

## Recreating Project
- To reproduce this project, download [acquire.py](https://github.com/aliciag92/classification-project/blob/main/acquire.py), [prepare.py](https://github.com/aliciag92/classification-project/blob/main/prepare.py), and [telco-churn-report.ipynb](https://github.com/aliciag92/classification-project/blob/main/telco-churn-report.ipynb) in your working directory and follow the steps from the pipeline process above.
- Do any additional exploring, modeling, and evaluating of your own to deliver any new information!