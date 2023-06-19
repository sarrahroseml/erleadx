""""
While the previous file iterated and trained 100 log reg models, this file only trains a single logreg model. 
The purpose is to train a logreg model using a random state that produces a high SN and high SP from previously, 
then extract the corresponding coefficients of the model to input into excel sheet. 

The logreg model uses a linear combination of variables which it inputs into the softmax function, so the coefficients represent the weightages 
on each of these variables within the linear combination. 

It's important to make sure that the same test_size and random_state is being used as what was generated previously. 
""""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Load the same dataset containing nodule characteristics & miRNA data
df = pd.read_csv('/Users/sarrahrose/Downloads/LogReg_NoduleChar+Biomarker_100.csv')  

# Extracting the features and labels
X = df.iloc[:, 2:22]  # selecting columns 3-22 as features 
y = df.iloc[:, 1]  # labels are in the second column

# Splitting the data into train and test sets in a stratified manner
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=93)

# Training the logistic regression model
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Get the confusion matrix
cm = confusion_matrix(y_test, y_pred)

TN, FP, FN, TP = cm.ravel()

# Calculate sensitivity and specificity
sensitivity = TP / (TP + FN)
specificity = TN / (TN + FP)

print(f'Sensitivity: {sensitivity}')
print(f'Specificity: {specificity}')

# Printing out the coefficients and the intercept
print("Coefficients: ", model.coef_)
print("Intercept: ", model.intercept_)


#Use these coefficients and input into the excel sheet. 
