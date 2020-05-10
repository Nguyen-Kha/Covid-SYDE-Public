


##################   D E M O G R A P H I C S   ################

# Where is your primary city of residence?
# Where is your primary country of residence?
# In which city were you primarily located in during the period of quarantine (March 13 - April 26)
# In which country were you primarily located in during the period of quarantine (March 13 - April 26)
def capitalize_string(word):
    return word.capitalize()

# How many courses were you taking?



##################   B E F O R E   A N D   D U R I N G   Q U A R A N T I N E   ################

# On average, how many hours of sleep did you get in a night [before quarantine]?
# Side Projects taking on [before quarantine]
# On average, how many hours a day did you spend Eating & Cooking [before quarantine] ?
# Hours spent "interneting" (Facebook, Instagram, Snapchat, Tiktok, Netflix, browsing, etc) in a day [before quarantine]
def clean_range_of_one(date):
    """ Potentially change the return type to <int>"""
    if(date == '0 - 1'):
        return '0.5'
    elif(date == '1 - 2' or date == '< 2' or date == '02-Jan'):
        return '1.5'
    elif(date == '> 2'or date == '2 - 3' or date == '03-Feb'):
        return '2.5'
    elif(date == '3 - 4' or date == '04-Mar'):
        return '3.5'
    elif(date == '< 5' or date == '05-Apr'):
        return '4.5'
    elif(date == '06-May'):
        return '5.5'
    elif(date == '07-Jun' or date == '6 +'):
        return '6.5'
    elif(date == '08-Jul'):
        return '7.5'
    elif(date == '09-Aug'):
        return '8.5'
    elif(date == '9 +' or date == '10-Sep'):
        return '9.5'
    # elif(date == '' ) # or whatever it is for NaN
    #     return # Whatever the mean is when we calculate it
    else:
        return date

# Study Habits [before quarantine] 
""" Potentially Reverse """
def reverse_scale(number, scale_number=7):
    return scale_number - number + 1    

# About how many hours a day did you spend outside your home [before quarantine] ?
# About how many hours a day did you spend socializing [before quarantine] ?
def clean_range_of_two(value):
    """ Potentially change the return type to <int>"""
    if(value == '0 - 2'):
        return '1'
    elif(value == '2 - 4' or value == '04-Feb'):
        return '3'
    elif(value == '4 - 6' or value == '06-Apr'):
        return '5'
    elif(value == '6 - 8' or value == '08-Jun'):
        return '7'
    elif(value == '8 - 10' or value == '10-Aug'):
        return '9'
    elif(value == '10 +'):
        return '11'
    # elif(value == '' ) # or whatever it is for NaN
    #     return # Whatever the mean is when we calculate it
    else:
        return value



# How many many people have you interacted with on an average day with classes? (Interaction defined by having at least a short conversation with person)
""" Mean range, remove people """





##################   E X A M S   A N D   A C A D E M I C S   ################
""" Might not need to do these ones """
# How long did you take to write each timed exam?
# How long did the SYDE 261 exam take you to complete?
# How long did the SYDE 285 Written portion take you to complete?

# In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 211] AND OTHERS
def remove_easiest_and_hardest(rank):
    if(rank == '1 (Hardest)'):
        return '1'
    elif(rank == '5 (Easiest)'):
        return '5'
    # elif(rank == 'N/A'):
    #     return # Whatever the mean for this is after we calculate it beforehand
    else:
        return rank

# Amount of hours spent studying for each exam [SYDE 211]
def hours_of_studying_exams(hours):
    """ Use this to calculate average. Keep the original when doing the data stuff"""
    if(hours == '0 - 4'):
        return '2'
    elif(hours == '5 - 9'):
        return '7'
    elif(hours == '10 - 14'):
        return '12'
    elif(hours == '15 - 19'):
        return '17'
    elif(hours == '20 - 24'):
        return '22'
    elif(hours = '24 +'):
        return '27'
    # else: # N/A or NaN
    #     return # the mean

def calculate_mean(values): # Data frame?
    # For loop and then size of dataframe column

# Stress level during a timed exam

# How did the quarantine effect your motivation to study? 

# How did quarantine affect your work ethic?

# How many hours did you spend on the following assignments? [SYDE 223 PE 2]
def hours_of_assignments(hours):
    """ Use this to calculate average. Keep the original when doing the data stuff"""
    if(hours == '0 - 4'):
        return '2'
    elif(hours == '4 - 8'):
        return '6'
    elif(hours == '8 - 12'):
        return '10'
    elif(hours == '12 - 16'):
        return '14'
    elif(hours == '16 - 20'):
        return '18'
    elif(hours == '20 - 24'):
        return '22'
    elif(hours = '24 +'):
        return '26'
    # else: # N/A or NaN
    #     return # the mean



##################   J O B S   /   C O - O P   ################



##################   M E N T A L   H E A L T H   ################
# How has quarantine affected your mental health?
""" This is the only question that has a scale of 5. Adjust scores accordingly 
    Multiply score taken in by 1.4 """
def adjust_5_to_7(score):
    return score * 1.4



##################   J U S T   F O R   F U N   ################

# How much money did you spend on Uber Eats/Equivalents?

