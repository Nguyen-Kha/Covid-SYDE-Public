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
        'Hours of Sleep per Night DQ',
        'Hours Spent Eating/Cooking per Day BQ',
        'Hours Spent Interneting per Day BQ',
        'Hours of Sleep per Night DQ',
        'Hours Spent Eating/Cooking per Day DQ',
        'Hours Spent Interneting per Day DQ'
    ]] = df[[
        'Hours of Sleep per Night DQ',
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

def clean_range_of_four(date):
    if(date == '09-May'):
        return '5 - 9'
    elif (date == '14-Oct'):
        return '10 - 14'

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