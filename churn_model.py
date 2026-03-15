import pandas as pd
import sqlite3
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

conn = sqlite3.connect('churn.db')
df = pd.read_sql_query("SELECT * FROM churn", conn)
conn.close()

print(df.head())
print(df.columns.tolist())
print(df.shape)

# Drop columns the model shouldn't use
X = df.drop(columns=['exited', 'churn_label'])

# Target variable
y = df['exited']

# Convert text columns to numbers
X = pd.get_dummies(X, columns=['geography', 'gender'], drop_first=True)

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training rows: {len(X_train)}")
print(f"Test rows: {len(X_test)}")
print(f"Features: {X.columns.tolist()}")

# create the model
model = LogisticRegression(max_iter=1000)

# train it on the training data
model.fit(X_train, y_train)

# use the model to predict on test data
y_pred = model.predict(X_test)

# see how accurate it was
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))