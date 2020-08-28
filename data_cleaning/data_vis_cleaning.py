"""
This file is to fix up the CSVs to display multiple choices rather than converting it to numerical values
If you need to convert it to a numerical value (so you can work with averages for analysis), use
covid_data_cleaning.py
"""

import pandas as pd

def clean_range_of_one(date):
    if(date == '02-Jan'):
        return '1 - 2'
    elif(date == '03-Feb'):
        return '2 - 3'
    elif(date == '04-Mar'):
        return '3 - 4'
    elif(date == '05-Apr'):
        return '4 - 5'
    elif(date == '06-May'):
        return '5 - 6'
    elif(date == '07-Jun'): 
        return '6 - 7'
    elif(date == '08-Jul'):
        return '7 - 8'
    elif(date == '09-Aug'):
        return '8 - 9'
    elif(date == '10-Sep'):
        return '9 - 10'
    else:
        return date

def clean_range_of_one_applymap(df):
    df[[
        'Hours of Sleep per Night BQ',
        'Hours Spent Eating/Cooking per Day BQ',
        'Hours Spent Interneting per Day BQ',
        'Hours of Sleep per Night DQ',
        'Hours Spent Eating/Cooking per Day DQ',
        'Hours Spent Interneting per Day DQ'
    ]] = df[[
        'Hours of Sleep per Night BQ',
        'Hours Spent Eating/Cooking per Day BQ',
        'Hours Spent Interneting per Day BQ',
        'Hours of Sleep per Night DQ',
        'Hours Spent Eating/Cooking per Day DQ',
        'Hours Spent Interneting per Day DQ'
    ]].applymap(clean_range_of_one)
    return df

def clean_range_of_two(date):
    if(date == '04-Feb'):
        return '2 - 4'
    elif(date == '06-Apr'):
        return '4 - 6'
    elif(date == '08-Jun'):
        return '6 - 8'
    elif(date == '10-Aug'):
        return '8 - 10'
    else:
        return date

def clean_range_of_two_applymap(df):
    df[[
        'Hours Spent Outside Home per Day BQ',
        'Hours Spent Socializing per Day BQ',
        'Hours Spent Outside Home per Day DQ',
        'Hours Spent Socializing per Day DQ',
    ]] = df[[
        'Hours Spent Outside Home per Day BQ',
        'Hours Spent Socializing per Day BQ',
        'Hours Spent Outside Home per Day DQ',
        'Hours Spent Socializing per Day DQ',
    ]].applymap(clean_range_of_two)
    return df

def clean_range_of_four(date):
    if(date == '09-May'):
        return '5 - 9'
    elif (date == '14-Oct'):
        return '10 - 14'
    else:
        return date

def clean_range_of_four_applymap(df):
    df[[
        'Hours Spent Studying For SYDE 211',
        'Hours Spent Studying For SYDE 223',
        'Hours Spent Studying For SYDE 261',
        'Hours Spent Studying For SYDE 283',
        'Hours Spent Studying For SYDE 285',
        'Hours Spent Studying For Electives',
        'Hours Spent on SYDE 223 Practice Exercise 2',
        'Hours Spent on SYDE 261 Project 2',
        'Hours Spent on SYDE 261 Project 3',
        'Hours Spent on SYDE 285 Term Project'
    ]] = df[[
        'Hours Spent Studying For SYDE 211',
        'Hours Spent Studying For SYDE 223',
        'Hours Spent Studying For SYDE 261',
        'Hours Spent Studying For SYDE 283',
        'Hours Spent Studying For SYDE 285',
        'Hours Spent Studying For Electives',
        'Hours Spent on SYDE 223 Practice Exercise 2',
        'Hours Spent on SYDE 261 Project 2',
        'Hours Spent on SYDE 261 Project 3',
        'Hours Spent on SYDE 285 Term Project'
    ]].applymap(clean_range_of_four)
    return df

def convert_string_to_list(string):
    string = string.split(',')
    return string

# there is an error in the next function
def convert_string_to_list_applymap(df):
    df[[
        'Reasons for Staying in Waterloo'
    ]] = df[[
        'Reasons for Staying in Waterloo'
    ]].applymap(convert_string_to_list)
    return df

# Reformat answers from column AH

# Multiple options column BS

#################
def execute_all_cleaning(df):
    df = clean_range_of_one_applymap(df)
    df = clean_range_of_two_applymap(df)
    df = clean_range_of_four_applymap(df)
    return df


df_dv_std = pd.read_csv('../PRIVATE-Covid-SYDE/csv/data_vis_std.csv')
df_dv_text = pd.read_csv('../PRIVATE-Covid-SYDE/csv/data_vis_text.csv')

df_dv_std = execute_all_cleaning(df_dv_std)
df_dv_text = execute_all_cleaning(df_dv_text)

path = r'C:\Users\Kha\Documents\Programming\Python\PRIVATE-Covid-SYDE\csv\\'
df_dv_std.to_csv(path + 'data_vis_std.csv')
df_dv_text.to_csv(path + 'data_vis_text.csv')