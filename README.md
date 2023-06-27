# erleadx

Overview: 

Generating_Combinations.py: To generate all possible combinations of n biomarkers. 
SNSPAUC.py: To generate the sensitivity, specificity and AUC values of each file of combinations of n biomarkers

LogReg_NoduleChar+Biomarker_100.csv: The data file suitable for logistic regression model containing nodule characteristics. 
Iterating_RS_LogReg.py: To iterate over 100 random states, train & test a logistic regression model, and output the sensitivity and specificty of these 100 models into a file. 
RegLogReg.py: To train a logistic regression model using the most favourable random states, then print out the coefficients of variables. 

umap_visualisation.py: To plot a UMAP plot from raw CT values. 
