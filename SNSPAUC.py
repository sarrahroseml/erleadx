""""
This file is meant to help identify the optimal combination of biomarkers. It reads the file generated from 'Generating_Combinations.py' and calculates
the SN, SP and AUC of each combination. 
""""

import pandas as pd
import csv

mean_biomarker1 = 30
mean_biomarker2 = 33.5
mean_biomarker3 = 26.5
mean_biomarker4 = 31
mean_biomarker5 = 33.5
mean_biomarker6 = 28
mean_biomarker7 = 24.8
mean_biomarker8 = 24.5
mean_biomarker9 = 36.5
mean_biomarker10 = 33.6
mean_biomarker11 = 31.5
mean_biomarker12 = 25
mean_biomarker13 = 21.9
mean_biomarker14 = 28.9
mean_biomarker15 = 19
mean_biomarker16 = 23.4

def read_combinations_from_csv(filename):
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            yield row

#Function to calculate AUC
def calculating_auc_gen():
    total_control = 56
    total_case = 44

    thresholds = [0,1, 2, 3, 4, 5, 6, 7, 8] #remember to adjust this according to number of biomarkers present (i.e. all possible risk scores)
    control_counts = []
    case_counts = []
    fpr_list = [1]
    tpr_list = [1]
    cumulative_control_count = 0
    cumulative_case_count = 0

    for threshold in thresholds:
        control_count = df_copy.loc[(df_copy['Sum'] == threshold) & (df_copy['Disease'] == 0)].shape[0]
        case_count = df_copy.loc[(df_copy['Sum'] == threshold) & (df_copy['Disease'] == 1)].shape[0]
        control_counts.append(control_count)
        case_counts.append(case_count)
        
        cumulative_control_count += control_count
        cumulative_case_count += case_count
        fpr_list.append(1 - (cumulative_control_count / total_control))
        tpr_list.append(1-(cumulative_case_count / total_case))
        
    auc_score = 0
    for i in range(1, len(fpr_list)):
        auc_score += (fpr_list[i-1] - fpr_list[i]) * tpr_list[i-1]

    return auc_score


subtraction_values = {'Biomarker 1': mean_biomarker1, 'Biomarker 2': mean_biomarker2, 'Biomarker 3': mean_biomarker3,
                      'Biomarker 4': mean_biomarker4, 'Biomarker 5': mean_biomarker5, 'Biomarker 6': mean_biomarker6,
                      'Biomarker 7': mean_biomarker7, 'Biomarker 8': mean_biomarker8, 'Biomarker 9': mean_biomarker9,
                      'Biomarker 11': mean_biomarker11,'Biomarker 12': mean_biomarker12, 'Biomarker 13': mean_biomarker13,
                      'Biomarker 14': mean_biomarker14, 'Biomarker 15': mean_biomarker15, 'Biomarker 16': mean_biomarker16
                      }

y = 9 #for 6 biomarkers (adjust accordingly). This y variable is used to mark the end range of columns of biomarkers to process. 
cutoff = 3 #Adjust accordingly
results = []

df = pd.read_csv(#file path for CSV file containing raw CT values) 

combinations_generator = read_combinations_from_csv(#file path for CSV file containing all possible combinations for n biomarkers)
for combination in combinations_generator:

    # Create a new subtraction dictionary based on the selected combination
    selected_subtraction_values = {col: subtraction_values[col] for col in combination if col in subtraction_values}

    # Update the subtraction values dictionary with the selected values
    subtraction_values.update(selected_subtraction_values)

    # Perform the calculations as in your current code
    df_copy = df.copy()
    biomarkers_to_drop = [col for col in df_copy.columns if col not in combination and col not in ['Patient', 'Disease', 'Stage']]
    df_copy = df_copy.drop(columns=biomarkers_to_drop)

    # Perform the remaining calculations
      # Iterate over each column
    columns = df_copy.columns
    for col in columns[3:y]:
        for index, row in df_copy.iterrows():
            # Subtract the specified value from each cell of the column
            df_copy.at[index, col] = df_copy.at[index, col] - subtraction_values[col]

        for index, row in df_copy.iterrows():
            # Subtract the specified value from each cell of the column
            df_copy.at[index, col] = 2 ** (-df_copy.at[index, col])

    df_copy["Sum"] = df_copy.apply(lambda x: sum(x[col] >= 2 for col in columns[3:y]), axis=1)

    #Making the predictions
    df_copy["Prediction"] = df_copy.apply(lambda x: 1 if x["Sum"] >= cutoff else 0, axis=1)

    # create a confusion matrix
    confusion_matrix = pd.crosstab(df_copy['Disease'], df_copy['Prediction'])

    # calculate true positive, true negative, false positive, and false negative
    true_positive = confusion_matrix[1][1]
    true_negative = confusion_matrix[0][0]
    false_positive = confusion_matrix[1][0]
    false_negative = confusion_matrix[0][1]

    print("tp",true_positive)
    print("fp",false_positive)
    print("tn",true_negative)
    print("fn",false_negative)

    # calculate sensitivity and specificity
    sensitivity = true_positive / (true_positive + false_negative)
    specificity = true_negative / (true_negative + false_positive)

    auc_scored = calculating_auc_gen()
    
    # Append the current combination and the sensitivity and specificity to the results list
    results.append({'combination': combination, 'sensitivity': sensitivity, 'specificity': specificity, 'auc':auc_scored})

# Write the results to a CSV file
with open('6combo_cutoff3_test.csv', 'w', newline='') as csvfile: #Adjust name of file accordingly
    fieldnames = ['combination', 'sensitivity', 'specificity', 'auc']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_NONNUMERIC)

    writer.writeheader()
    for result in results:
        result['sensitivity'] = format(result['sensitivity'], '.5f')
        result['specificity'] = format(result['specificity'], '.5f')
        writer.writerow(result)

