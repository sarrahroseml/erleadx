""""
This file is meant to iterate thrugh 100 random states (how the data is shuffled), and train a logistic regression model on each of these random states.
It outputs a csv file with the random state the logreg model is using, sensitivity and specificity for that model. 
The purpose of this is to find the specific logreg models which output a high SN and SP. Then use the test_size and random_state values in file 
""""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

# Load the csv dataset containing nodule characteristics and miRNA data. 
df = pd.read_csv('#Load LogReg Dataset')

X = df.iloc[:, 2:22]
y = df.iloc[:, 1]

results = pd.DataFrame(columns=['Random_State', 'Sensitivity', 'Specificity'])

for state in range(101):
    # Split the dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=state, stratify=y) #Specify test_size here. 
                                                                                                               #Make sure it matches with the single logreg file later. 

    # Initialize logistic regression model
    log_reg = LogisticRegression()

    # Fit the model to the training data
    log_reg.fit(X_train, y_train)

    # Predict the labels of the test set
    y_pred = log_reg.predict(X_test)

    # Get the confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    TN, FP, FN, TP = cm.ravel()

    # Calculate sensitivity and specificity
    sensitivity = TP / (TP + FN)
    specificity = TN / (TN + FP)

    # Add results to DataFrame
    results = results.append({'Random_State': state, 'Sensitivity': sensitivity, 'Specificity': specificity}, ignore_index=True)

# Save results to CSV
results.to_csv('22may_log_reg_0.25_TESTcsv', index=False) #Edit the filename accordingly here
