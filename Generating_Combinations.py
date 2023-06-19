""""
This file is to generate all possible combinations of n biomarkers, where n is specified below. It outputs a csv file, 
where each row is a specific combination of biomarkers 
""""


import itertools
import pandas as pd

biomarkers = ['Biomarker 1', 'Biomarker 2', 'Biomarker 3', 'Biomarker 4', 'Biomarker 5', 'Biomarker 6',
              'Biomarker 7', 'Biomarker 8', 'Biomarker 9', 'Biomarker 10', 'Biomarker 11', 'Biomarker 12',
              'Biomarker 13', 'Biomarker 14', 'Biomarker 15', 'Biomarker 16']

combinations = list(itertools.combinations(biomarkers, 6)) #Specify the number of biomarkers here

#Edit based on number of biomarkers desired
df = pd.DataFrame(combinations, columns=[' B 1', 'B 2', 'B 3',
                                         'B 4', 'B 5', 'B 6'])

df.to_csv('29MAY_biomarker_combination_6.csv', index=False) #Edit the filename here
