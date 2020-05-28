"""
This file is used to convert some CSV values into numerical values
For data visulization purposes, use data_vis_cleaning.py
"""
import pandas as pd


# How many courses were you taking?
def clean_amount_courses(courses):
    if(courses == '0 - 4'):
        return 4
    elif(courses == '7+'):
        return 7
    else: 
        return courses


##################   B E F O R E   A N D   D U R I N G   Q U A R A N T I N E   ################

# On average, how many hours of sleep did you get in a night [before quarantine]?
# On average, how many hours a day did you spend Eating & Cooking [before quarantine] ?
# Hours spent "interneting" (Facebook, Instagram, Snapchat, Tiktok, Netflix, browsing, etc) in a day [before quarantine]
def clean_range_of_one(date):
    """ Potentially change the return type to <int>"""
    if(date == '0 - 1'):
        return 0.5
    elif(date == '1 - 2' or date == '< 2' or date == '02-Jan'):
        return 1.5
    elif(date == '> 2'or date == '2 - 3' or date == '03-Feb'):
        return 2.5
    elif(date == '3 - 4' or date == '04-Mar'):
        return 3.5
    elif(date == '< 5' or date == '05-Apr' or date == '4 - 5'):
        return 4.5
    elif(date == '06-May' or date == '> 5'):
        return 5.5
    elif(date == '07-Jun' or date == '6 +'):
        return 6.5
    elif(date == '08-Jul'):
        return 7.5
    elif(date == '09-Aug'):
        return 8.5
    elif(date == '9 +' or date == '10-Sep'):
        return 9.5
    else:
        return date

# Side Projects taking on [before quarantine]
# CR / NCR
def clean_increase_value_by_one(value):
    if(value == '> 2'):
        return 3
    elif(value == '6 +'):
        return 6
    else:
        return value

# Study Habits [before quarantine] 
""" Potentially Reverse """
def reverse_scale(number, scale_number=7):
    return scale_number - number + 1    

# About how many hours a day did you spend outside your home [before quarantine] ?
# About how many hours a day did you spend socializing [before quarantine] ?
def clean_range_of_two(value):
    """ Potentially change the return type to <int>"""
    if(value == '0 - 2'):
        return 1
    elif(value == '2 - 4' or value == '04-Feb'):
        return 3
    elif(value == '4 - 6' or value == '06-Apr'):
        return 5
    elif(value == '6 - 8' or value == '08-Jun'):
        return 7
    elif(value == '8 - 10' or value == '10-Aug'):
        return 9
    elif(value == '10 +'):
        return 11
    # elif(value == '' ) # or whatever it is for NaN
    #     return # Whatever the mean is when we calculate it
    else:
        return value



# How many many people have you interacted with on an average day with classes? (Interaction defined by having at least a short conversation with person)
""" Mean range, remove people """
def clean_people_interaction(people):
    if(people == '0 - 2 people'):
        return 1
    elif(people == '3 - 5 people'):
        return 4
    elif(people == '6 - 10 people'):
        return 8
    elif(people == '11 - 20 people'):
        return 15
    elif(people == '20 + people'):
        return 25
    else:
        return None
    

##################   E X A M S   A N D   A C A D E M I C S   ################
""" Might not need to do these ones """

# How long did the SYDE 261 exam take you to complete?
def clean_261_exam_time(time):
    if(time == 'Less than 2.5 hours'):
        return 1.5
    elif(time == '2.5 - 4 hours'):
        return 3.25
    elif(time == '4 - 6 hours'):
        return 5
    elif(time == '6 + hours'):
        return 7
    else:
        return time

# How long did the SYDE 285 Written portion take you to complete?
def clean_285_exam_time(time):
    if(time == 'Less than 1.5 hours'):
        return 0.75
    elif(time == '1.5 - 3 hours'):
        return 2.25
    elif(time == '3 - 4.5 hours'):
        return 3.75
    elif(time == '4.5 - 6 hours'):
        return 5.25
    elif(time == '6 + hours'):
        return 6.75
    else:
        return time

# Amount of hours spent studying for each exam [SYDE 211]
def clean_hours_of_studying_exams(hours):
    """ Use this to calculate average. Keep the original when doing the data stuff"""
    if(hours == '0 - 4'):
        return 2
    elif(hours == '5 - 9'):
        return 7
    elif(hours == '10 - 14'):
        return 12
    elif(hours == '15 - 19'):
        return 17
    elif(hours == '20 - 24'):
        return 22
    elif(hours == '24 +'):
        return 27
    else:
        return hours

def clean_mark_walking_in(marks):
    if(marks == '0 - 49'):
        return 32
    elif(marks == '50 - 59'):
        return 55
    elif(marks == '60 - 69'):
        return 65
    elif(marks == '70 - 79'):
        return 75
    elif(marks == '80 - 89'):
        return 85
    elif(marks == '90 - 100'):
        return 95
    else:
        return marks

# How many hours did you spend on the following assignments? [SYDE 223 PE 2]
def clean_hours_of_assignments(hours):
    """ Use this to calculate average. Keep the original when doing the data stuff
        Incorrect answer options, missing 16 - 20. """
    if(hours == '0 - 4'):
        return 2
    elif(hours == '4 - 8' or hours == '08-Apr'):
        return 6
    elif(hours == '8 - 12' or hours == '12-Aug'):
        return 10
    elif(hours == '12 - 16' or hours =='16-Dec'):
        return 15
    # elif(hours == '16 - 20'):
    #     return 18
    elif(hours == '20 - 24'):
        return 21
    elif(hours == '24 +'):
        return 26
    else:
        return hours


##################   M E N T A L   H E A L T H   ################

# How has quarantine affected your mental health?
""" This is the only question that has a scale of 5. Adjust scores accordingly 
    Multiply score taken in by 1.4 """
def adjust_5_to_7(score):
    return score * 1.4

# Calling Family
def clean_calling_family(time):
    if(time == '4 + times a day'):
        return 5
    elif(time == '2 - 3 times a day'):
        return 3
    elif(time == 'Every day'):
        return 1
    elif(time == '2 - 3 times a week'):
        return 0.4
    elif(time == 'Once a week '):
        return 0.14
    elif(time == 'Once every 2 weeks'):
        return 0.07
    elif(time == 'Once a month'):
        return 0.03
    elif(time == 'Never'):
        return 0
    else: 
        return time
    
    

##################   J U S T   F O R   F U N   ################

# Dating App Swipes
# Video Games
def clean_dating_video_games(time):
    if(time == 'Several Hours a Day'):
        return 3
    elif(time == '1 Hour a Day'):
        return 1
    elif(time == 'A couple of minutes a day'):
        return 0.5
    elif(time == 'A couple of times a week'):
        return 0.25
    elif(time == 'Once a Week'):
        return 0.14
    elif(time == 'Once every 2 weeks'):
        return 0.07
    elif(time == 'Once a Month'):
        return 0.03
    elif(time == 'I did not use any dating apps' or time == 'I did not play any video games'):
        return 0
    else:
        return time
    
####################################################################################
##################   H E L P E R S   ################

def replace_nulls_with_mean(df, column_name):
    mean = df[column_name].mean()
    df[column_name].fillna(mean, inplace = True)
    return df

def replace_nulls_with_zero(df, column_name):
    df[column_name].fillna(0, inplace = True)
    return df

def replace_nulls_with_unanswered(df, column_name):
    df[column_name].fillna('No Answer', inplace = True)
    return df

####################################################################################
################ FUNCTIONS TO CALL FUNCTIONS #############
 
def number_of_courses_apply(df):
    df[['Courses Taken']] = df[['Courses Taken']].apply(clean_amount_courses)

def range_one_applymap(df):
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

def increase_one_applymap(df):
    df[[
        'Side Projects BQ',
        'Side Projects DQ',
        'Courses CR/NCR-ed'
    ]] = df[[
        'Side Projects BQ',
        'Side Projects DQ',
        'Courses CR/NCR-ed'
    ]].applymap(clean_increase_value_by_one)
    return df

def range_two_applymap(df):
    df[[
        'Hours Spent Outside Home per Day BQ',
        'Hours Spent Socializing per Day BQ',
        'Hours Spent Outside Home per Day DQ',
        'Hours Spent Socializing per Day DQ'
    ]] = df[[
        'Hours Spent Outside Home per Day BQ',
        'Hours Spent Socializing per Day BQ',
        'Hours Spent Outside Home per Day DQ',
        'Hours Spent Socializing per Day DQ'
    ]].applymap(clean_range_of_two)
    return df

def interaction_applymap(df):
    df[[
        'Amount of People Interacted With per Day BQ',
        'Amount of People Interacted With per Day DQ'
    ]] = df[[
        'Amount of People Interacted With per Day BQ',
        'Amount of People Interacted With per Day DQ'
    ]].applymap(clean_people_interaction)
    return df

def _261_apply(df):
    df[['Time to Finish SYDE 261 Exam']] = df[['Time to Finish SYDE 261 Exam']].apply(clean_261_exam_time)
    return df

def _285_apply(df):
    df[['Time to Finish SYDE 285 Written Portion']] = df[['Time to Finish SYDE 285 Written Portion']].apply(clean_285_exam_time)
    return df

def hours_studying_applymap(df):
    df[[
        'Hours Spent Studying For SYDE 211',
        'Hours Spent Studying For SYDE 223',
        'Hours Spent Studying For SYDE 261',
        'Hours Spent Studying For SYDE 283',
        'Hours Spent Studying For SYDE 285'
    ]] = df[[
        'Hours Spent Studying For SYDE 211',
        'Hours Spent Studying For SYDE 223',
        'Hours Spent Studying For SYDE 261',
        'Hours Spent Studying For SYDE 283',
        'Hours Spent Studying For SYDE 285'
    ]].applymap(clean_hours_of_studying_exams)
    return df

def marks_applymap(df):
    df[[
        'SYDE 211 Mark Before Exam',
        'SYDE 223 Mark Before Exam',
        'SYDE 261 Mark Before Exam',
        'SYDE 283 Mark Before Exam',
        'SYDE 285 Mark Before Exam'
    ]] = df[[
        'SYDE 211 Mark Before Exam',
        'SYDE 223 Mark Before Exam',
        'SYDE 261 Mark Before Exam',
        'SYDE 283 Mark Before Exam',
        'SYDE 285 Mark Before Exam'
    ]].applymap(clean_mark_walking_in)
    return df

def hours_assignments_applymap(df):
    df[[
        'Hours Spent on SYDE 223 Practice Exercise 2',
        'Hours Spent on SYDE 261 Project 2',
        'Hours Spent on SYDE 261 Project 3',
        'Hours Spent on SYDE 285 Term Project'
    ]] = df[[
        'Hours Spent on SYDE 223 Practice Exercise 2',
        'Hours Spent on SYDE 261 Project 2',
        'Hours Spent on SYDE 261 Project 3',
        'Hours Spent on SYDE 285 Term Project'
    ]].applymap(clean_hours_of_assignments)
    return df

def adjust_7_apply(df):
    df[['Effects on Mental Health']] = df[['Effects on Mental Health']].apply(adjust_5_to_7)
    return df

def calling_family_apply(df):
    df[['Amount of Times Called Friends/Family']] = df[['Amount of Times Called Friends/Family']].apply(clean_calling_family)
    return df

def dating_video_games_applymap(df):
    df[[
        'Time Spent Swiping on Dating Apps',
        'Amount of Time Playing Video Games'
    ]] = df[[
        'Time Spent Swiping on Dating Apps',
        'Amount of Time Playing Video Games'
    ]].applymap(clean_dating_video_games)
    return df

def execute_all_numerical_cleaning(df):
    df = range_one_applymap(df)
    df = increase_one_applymap(df)
    df = range_two_applymap(df)
    df = interaction_applymap(df)
    df = _261_apply(df)
    df = _285_apply(df)
    df = hours_studying_applymap(df)
    df = marks_applymap(df)
    df = hours_assignments_applymap(df)
    df = adjust_7_apply(df)
    df = calling_family_apply(df)
    df = dating_video_games_applymap(df)

    ##############  Clean data before processing mean ############
    
    # Check what to do for Hours Spent Studying For Electives
    columns_to_replace_with_mean = [
        'Time to Finish SYDE 261 Exam',
        'Time to Finish SYDE 285 Written Portion',
        'SYDE 223 Exam Difficulty',
        'SYDE 261 Exam Difficulty',
        'Hours Spent Studying For SYDE 211',
        'Hours Spent Studying For SYDE 223',
        'Hours Spent Studying For SYDE 261',
        'Hours Spent Studying For SYDE 283',
        'Hours Spent Studying For SYDE 285',
        'SYDE 211 Mark Before Exam ',
        'SYDE 223 Mark Before Exam ',
        'SYDE 261 Mark Before Exam ',
        'SYDE 283 Mark Before Exam ',
        'SYDE 285 Mark Before Exam ',
        'Motivation to Study DQ',
        'Work Ethic DQ',
        'Hours Spent on SYDE 223 Practice Exercise 2',
        'Hours Spent on SYDE 261 Project 2',
        'Hours Spent on SYDE 261 Project 3',
        'Hours Spent on SYDE 285 Term Project',
        'Easiness of Learning Online',
        'Apps Sent',
        'Interviews Received',
        'Amount of Times Broken Social Distancing',
        'Rolls of Toilet Paper Bought',
        'Days Spent in Pyjamas',
        'Dalgona Coffees Made',
    ]

    columns_to_replace_with_zero = [

    ]

    columns_to_replace_with_unanswered = [
        'Move-Out Date',
        'Learning Style',
    ]
    for i in range(0, len(columns_to_replace_with_mean)):
        df = replace_nulls_with_mean(df, columns_to_replace_with_mean[i])
    
    for i in range(0, len(columns_to_replace_with_unanswered)):
        df = replace_nulls_with_unanswered(df, columns_to_replace_with_unanswered[i])

    # for i in range(0, len(columns_to_replace_with_zero)):
    #     df = replace_nulls_with_zero(df, columns_to_replace_with_zero[i])

    return df

####################################################################################

df_num_std = pd.read_csv('')
df_num_text = pd.read_csv('')
