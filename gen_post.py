#!/usr/bin/env python
# coding: utf-8

# # Generating Post Variables
# - Timing of Reforms comes from Simon (2005)
# - Data is stored in an Excel spreadsheet titled "reform_timing"

import pandas as pd
from ipywidgets import interact
import numpy as np



get_ipython().system('pip install openpyxl')


#Reading in Excel sheet into a pandas dataframe
reform_timing = pd.read_excel('reform_timing.xlsx')
reform_timing = reform_timing.fillna(0) #filling missing values with 0 for easier manipulation


#'states' is a dictionary that matches state abbreviations (NY, CA, TX, etc.) to its designated state code in the CPS
# Each state abbreviation is its own key
states = {
    'AK': 2,
    'AL': 1,
    'AR': 5,
    'AZ': 4,
    'CA': 6,
    'CO': 8,
    'CT': 9,
    'DC': 11,
    'DE': 10,
    'FL': 12,
    'GA': 13,
    'HI': 15,
    'IA': 19,
    'ID': 16,
    'IL': 17,
    'IN': 18,
    'KS': 20,
    'KY': 21,
    'LA': 22,
    'MA': 25,
    'MD': 24,
    'ME': 23,
    'MI': 26,
    'MN': 27,
    'MO': 29,
    'MS': 28,
    'MT': 30,
    'NC': 37,
    'ND': 38,
    'NE':31,
    'NH': 33,
    'NJ': 34,
    'NM': 35,
    'NV': 32,
    'NY': 36,
    'OH': 39,
    'OK': 40,
    'OR': 41,
    'PA': 42,
    'RI': 44,
    'SC': 45,
    'SD': 46,
    'TN': 47,
    'TX': 48,
    'UT': 49,
    'VA': 51,
    'VT': 50,
    'WA': 53,
    'WI': 55,
    'WV': 54,
    'WY': 56
}



#Converting values from float to int
#May be a better way to do this with looping over specific columns, but for now I just did it manually
reform_timing = reform_timing.astype({'f_start': 'int'})
reform_timing = reform_timing.astype({'f_end': 'int'})
reform_timing = reform_timing.astype({'p_start': 'int'})
reform_timing = reform_timing.astype({'p_end': 'int'})
reform_timing = reform_timing.astype({'bb_start': 'int'})
reform_timing = reform_timing.astype({'bb_end': 'int'})



#Looping thorugh rows to generate a list of state code values
#Value from State column (ex: "NY") gets matched with its associated key in the state abbreviation dictionary.
code_list = []
for row in reform_timing.to_records():
    state = row['State']
    state_code = states[f'{state}']
    code_list.append(state_code)




reform_timing['State_codes'] = code_list #Create a new dataframe column that matches the state abbreviation with its associated state code




reform_timing


# # Post 1: Full Reform



#Code to generate Stata code for full reform variable
for row in reform_timing.to_records(): #Loop through each row of the dataframe
    if (row['f_start'] != 0) & (row['f_end'] != 0): #Only include values that are not missing (!=0)
        print(f"(statefip == {row['State_codes']} & (year >= {row['f_start']} & year <= {row['f_end']})) |",end = "")


# # Post 2: Partial Reform


#Partial reform. Same logic as full reform loop
for row in reform_timing.to_records():
    if (row['p_start'] != 0) & (row['p_end'] != 0):
        print(f"(statefip == {row['State_codes']} & (year >= {row['p_start']} & year <= {row['p_end']})) |",end = "")


# # Post 3: Barebones Reform




#Barebones reform. Same logic as other reforms
for row in reform_timing.to_records():
    if (row['bb_start'] != 0) & (row['bb_end'] != 0):
        print(f"(statefip == {row['State_codes']} & (year >= {row['bb_start']} & year <= {row['bb_end']})) |",end = "")

