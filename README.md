# Bank-Churn-Analysis
## Overview
A analysis project that builds an ETL pipeline to clean 
and transform bank customer data, analyzes churn patterns using SQL, and 
builds a machine learning model to predict which customers are likely to leave.

## Tools & Technologies
- **Python** — ETL pipeline, machine learning
- **SQL**
- **DBeaver** — SQL querying
- **Libraries** — pandas, scikit-learn, sqlite3

## Key SQL Findings
*  Overall 20.37% churn rate
*  German customers churn at twice the rate of French and Spanish customers (32% vs 16%)
*  Female customers churn at a significantly higher rate than male customers (25% vs 16%)
*  Churned customers had significantly higher average balances ($91K) than retained customers ($73K), suggesting high value customers are at greater risk of churn
*  Customers with 2 products had the lowest churn rate (8%) while customers with 3-4 products churned at 83-100%, suggesting over selling is a major churn driver
*  Credit card ownership does not have much impact on churn rate (20.8% vs 20.2%)
*  Tenure has no meaningful impact on churn (customers leave regardless of how long they've been with the bank)
*  Inactive members churn at nearly double the rate of active members (27% vs 14%)

## Machine Learning Model
Built a logistic regression model using scikit-learn to predict customer churn, 
achieving 81.4% accuracy on a test set of 2,000 customers.
* Features used: 
credit score, age, tenure, balance, number of products, 
credit card status, active member status, estimated salary, geography, gender

## How to Run
1. Clone the repo
2. Install dependencies:
pip install pandas scikit-learn
3. Run the ETL pipeline:
python etl_pipeline.py
4. Run the ML model:
python churn_model.py
5. Open churn.db in DBeaver to run SQL queries
