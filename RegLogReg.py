import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Assuming df is your DataFrame
df = pd.read_csv('/Users/sarrahrose/Downloads/LogReg_NoduleChar+Biomarker_100.csv')  # replace 'your_file.csv' with your data file

# Extracting the features and labels
X = df.iloc[:, 2:22]  # selecting columns 3-22 as features 
y = df.iloc[:, 1]  # labels are in the second column

# Splitting the data into train and test sets in a stratified manner
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=93)

# Training the logistic regression model
model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

# Printing out the coefficients and the intercept
print("Coefficients: ", model.coef_)
print("Intercept: ", model.intercept_)

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
