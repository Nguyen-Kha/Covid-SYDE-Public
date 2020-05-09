


##################   D E M O G R A P H I C S   ################

# Where is your primary city of residence?
# Where is your primary country of residence?
# In which city were you primarily located in during the period of quarantine (March 13 - April 26)
# In which country were you primarily located in during the period of quarantine (March 13 - April 26)
def capitalize_string(word):
    return word.capitalize()



##################   B E F O R E   A N D   D U R I N G   Q U A R A N T I N E   ################

# On average, how many hours of sleep did you get in a night [before quarantine]?
def date_to_numbered_string(date):
    if(date == '0 - 1'):
        return '0.5'
    elif(date == '1 - 2'):
        return '1.5'
    elif(date == '< 2'):
        return '1.5'
    elif(date == '> 2'):
        return '2.5'
    elif(date == '2 - 3'):
        return '2.5'
    elif(date == '3 - 4'):
        return '3.5'
    elif(date == '< 5'):
        return '4.5'
    elif(date == '06-May'):
        return '5.5'
    elif(date == '07-Jun'):
        return '6.5'
    elif(date == '08-Jul'):
        return '7.5'
    elif(date == '09-Aug'):
        return '8.5'
    elif(date == '9 +'):
        return '9.5'

# Study Habits [before quarantine] 
""" Potentially Reverse """
def reverse_scale(number, scale_number=7):
    return scale_number - number + 1    

# Side Projects taking on [before quarantine]

# On average, how many hours a day did you spend Eating & Cooking [before quarantine] ?

# About how many hours a day did you spend outside your home [before quarantine] ?

# About how many hours a day did you spend socializing [before quarantine] ?

# How many many people have you interacted with on an average day with classes? (Interaction defined by having at least a short conversation with person)
""" Mean range, remove people """

# Hours spent "interneting" (Facebook, Instagram, Snapchat, Tiktok, Netflix, browsing, etc) in a day [before quarantine]



##################   E X A M S   A N D   A C A D E M I C S   ################

# How long did you take to write each timed exam?

# How long did the SYDE 261 exam take you to complete?

# How long did the SYDE 285 Written portion take you to complete?

# In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 211] AND OTHERS

# Amount of hours spent studying for each exam [SYDE 211]

# Stress level during a timed exam

# How did the quarantine effect your motivation to study? 

# How did quarantine affect your work ethic?

# How many hours did you spend on the following assignments? [SYDE 223 PE 2]



##################   J O B S   /   C O - O P   ################



##################   J U S T   F O R   F U N   ################

# How much money did you spend on Uber Eats/Equivalents?