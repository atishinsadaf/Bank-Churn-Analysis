import pandas as pd
import sqlite3

def extract(filepath):
    df = pd.read_csv(filepath)
    return df

# Transform
def transform(df):
    # Change columns to snake case
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('-', '_')

    # Strip whitespace
    df = df.apply(lambda col: col.str.strip() if col.dtype == 'object' else col)

    # Drop unnecessary columns
    df = df.drop(columns=['rownumber', 'customerid', 'surname'])

    # Add Churned column
    df['churn_label'] = df['exited'].apply(lambda x: 'Churned' if x==1 else 'Retained')

    return df

def validate(df):
    assert len(df) > 9000
    assert df['exited'].isin([0, 1]).all()
    assert df['creditscore'].notnull().sum() > 0
    print ('Validation passed')

def load(df):
    conn = sqlite3.connect('churn.db')
    df.to_sql('churn', conn, if_exists='replace', index=False)
    conn.close()
    print ('Loading complete into churn.db')

def run():
    df = extract('Churn_Modelling.csv')
    df = transform(df)
    validate(df)
    load(df)
    print ('Pipeline complete')

run()