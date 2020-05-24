import pandas as pd


def rename_column_headers(df):
    df = df.rename(columns = {
        'If you lived off campus, when did you move out of Waterloo': 'Move-Out Date',
        'If you stayed in Waterloo for the majority of the quarantine period, why?': 'Reasons for Staying in Waterloo',
        'If you were not in Waterloo for the majority of the quarantine period, why?': 'Reasons for Leaving Waterloo',
        'How many courses were you taking?': 'Courses Taken',
        'What is your main learning style?': 'Learning Style',

        'On average, how many hours of sleep did you get in a night [before quarantine]?': 'Hours of Sleep per Night BQ',
        'On average, what time did you fall asleep [before quarantine]?': 'Time Slept BQ',
        'On average, what time did you wake up [before quarantine]?': 'Time Woke Up BQ',
        'Study Habits [before quarantine]': 'Study Habits BQ',
        'Side Projects taking on [before quarantine]': 'Side Projects BQ',
        'On average, how many hours a day did you spend Eating & Cooking [before quarantine] ?': 'Hours Spent Eating/Cooking per Day BQ',
        'About how many hours a day did you spend outside your home [before quarantine] ?': 'Hours Spent Outside Home per Day BQ',
        'About how many hours a day did you spend socializing [before quarantine] ?': 'Hours Spent Socializing per Day BQ',
        'How many many people have you interacted with on an average day with classes? (Interaction defined by having at least a short conversation with person)': 'Amount of People Interacted With per Day BQ',
        'How often did you attend classes [before quarantine] ?': 'Class Attendance BQ',
        'How many days per week did you do intense exercise over half an hour (gym, intramurals, running, sport) [before quarantine]': 'Days of Exercise per Week BQ',
        'Hours spent "interneting" (Facebook, Instagram, Snapchat, Tiktok, Netflix, browsing, etc) in a day [before quarantine]': 'Hours Spent Interneting per Day BQ',
        'On an average day, how stressed did you feel?': 'Average Stress Levels BQ',

        'On average, how many hours of sleep did you get in a night?': 'Hours of Sleep per Night DQ',
        'On average, what time did you fall asleep?': 'Time Slept DQ',
        'On average, what time did you wake up?': 'Time Woke Up DQ',
        'Study Habits [during quarantine]': 'Study Habits DQ',
        'Side Projects taking on': 'Side Projects DQ',
        'On average, how many hours did you spend Eating & Cooking?': 'Hours Spent Eating/Cooking per Day DQ',
        'About how many hours a day did you spend outside your home [during quarantine]?': 'Hours Spent Outside Home per Day DQ',
        'About how many hours a day did you spend socializing [during quarantine]?': 'Hours Spent Socializing per Day DQ',
        'How many many people have you interacted with on a school day during quarantine? (Interaction defined by having at least a short conversation with person either through Skype, phone or a messaging platform)': 'Amount of People Interacted With per Day DQ',
        'How often did you attend classes [during quarantine] ?': 'Class Attendance DQ',
        'How many days per week did you do intense exercise over half an hour (gym, intramurals, running, sport) [during quarantine]': 'Days of Exercise per Week DQ',
        'Time spent "interneting" (Facebook, Instagram, Snapchat, Tiktok, Netflix, browsing, etc) in a day [during quarantine]': 'Hours Spent Interneting per Day DQ',
        'On an average day, how stressed did you feel?.1': 'Average Stress Levels DQ',

        'Difficulty of each online exam compared to an in class exam': 'Difficulty of Online vs In Class Exam',
        'How long did you take to write each timed exam?': 'Exam Finishing Status',
        'How long did the SYDE 261 exam take you to complete?': 'Time to Finish SYDE 261 Exam',
        'How long did the SYDE 285 Written portion take you to complete?': 'Time to Finish SYDE 285 Written Portion',
        'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 211]': 'SYDE 211 Exam Difficulty',
        'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 223]': 'SYDE 223 Exam Difficulty',
        'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 261]': 'SYDE 261 Exam Difficulty',
        'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 283]': 'SYDE 283 Exam Difficulty',
        'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 285]': 'SYDE 285 Exam Difficulty',
        'Amount of hours spent studying for each exam [SYDE 211]': 'Hours Spent Studying For SYDE 211',
        'Amount of hours spent studying for each exam [SYDE 223]': 'Hours Spent Studying For SYDE 223',
        'Amount of hours spent studying for each exam [SYDE 261]': 'Hours Spent Studying For SYDE 261',
        'Amount of hours spent studying for each exam [SYDE 283]': 'Hours Spent Studying For SYDE 283',
        'Amount of hours spent studying for each exam [SYDE 285]': 'Hours Spent Studying For SYDE 285',
        'Amount of hours spent studying for each exam [Electives]': 'Hours Spent Studying For Electives',
        'Which marks did you walk into each exam with? [SYDE 211]': 'SYDE 211 Mark Before Exam',
        'Which marks did you walk into each exam with? [SYDE 223]': 'SYDE 223 Mark Before Exam',
        'Which marks did you walk into each exam with? [SYDE 261]': 'SYDE 261 Mark Before Exam',
        'Which marks did you walk into each exam with? [SYDE 283]': 'SYDE 283 Mark Before Exam',
        'Which marks did you walk into each exam with? [SYDE 285]': 'SYDE 285 Mark Before Exam',
        'Stress level during a timed exam': 'Timed Exam Stress Level',
        'Rank your Term Average from Lowest (1) to Highest (3)  [1A]': 'Rank of 1A Average',
        'Rank your Term Average from Lowest (1) to Highest (3)  [1B]': 'Rank of 1B Average',
        'Rank your Term Average from Lowest (1) to Highest (3)  [2A]': 'Rank of 2A Average',
        'How did the quarantine effect your motivation to study? ': 'Motivation to Study DQ',
        'How did quarantine affect your work ethic?': 'Work Ethic DQ',
        'How many hours did you spend on the following assignments? [SYDE 223 PE 2]': 'Hours Spent on SYDE 223 Practice Exercise 2',
        'How many hours did you spend on the following assignments? [SYDE 261 Project 2]': 'Hours Spent on SYDE 261 Project 2',
        'How many hours did you spend on the following assignments? [SYDE 261 Project 3]': 'Hours Spent on SYDE 261 Project 3',
        'How many hours did you spend on the following assignments? [SYDE 285 Term Project]': 'Hours Spent on SYDE 285 Term Project',
        'Ease of learning online (comparing to in-class)': 'Easiness of Learning Online',
        'How many courses do you plan on CR/NCR-ing?': 'Courses CR/NCR-ed',
        'Main Methods of Studying': 'Methods of Studying',
        
        'What type of roles were you going for?': 'Roles Desired',
        'How many applications did you send out?': 'Apps Sent',
        'How many interviews did you receive?': 'Interviews Received',
        'Was there a large amount of postings for your ideal positions on WaterlooWorks?': 'Quantity of Postings of WW',
        'At any point in the term, did you have an offer for a co-op job?': 'Had an Offer',
        'At any point in the term, did you receive an offer that got cancelled?': 'Had Cancelled Offer',

        'Which field was this cancelled job in?': 'Field of Cancelled Job',
        'In which city would your job have been located in?': 'City of Cancelled Job',
        'In which country would your job have been located in?': 'Country of Cancelled Job',
        'What would have been the size of your company': 'Company Size of Cancelled Job',
        'What is the net worth of that company?': 'Company Net Worth of Cancelled Job',
        'Which Industry best describes the company you would have worked for?': 'Industry of Cancelled Job',
        'When was your job cancelled?': 'Date of Job Cancellation',
        'Did you end up finding a job as of May 1st?': 'Found Job After Cancellation',

        'Which field was this job in?': 'Field of Job',
        'In which city is your job located?': 'City of Job',
        'In which country is your job located?': 'Country of Job',
        'Is your job currently remote?': 'Remote Job',
        'What is the size of your company': 'Size of Company',
        'What is the net worth of your company?': 'Company Net Worth',
        'Which Industry best describes the company you are for?': 'Industry of Job',
        'When did you get your job?': 'Date of Job Offer',

        'Are you still actively seeking a co-op position?': 'Still Seeking Job',
        'How have you been looking for co-op jobs?': 'Job Search Methods',
        'How are you planning on spending your spring term?': 'Spring Term Plans',

        'How worried are you on your current financial situation during this quarantine period?': 'Worried About Finances',
        'Have you been negatively affected financially by COVID-19 in any way?': 'Affected Negatively Financially',
        'What are your main financial concerns of COVID-19?': 'Financial Concerns',
        'Do you qualify for CESB / CERB?': 'Qualify CERB/CESB',
        'Did you apply for CESB / CERB?': 'Applied CERB/CESB',
        'Have your spending habits increased or decreased?': 'Change in Spending Habits',
        'Which of the following items did you spend most of your money on during the quarantine period? Choose 3.': 'Expenditures',
        'How do you plan on financing your 2B term?': 'Method of Financing 2B',

        'How many times did you break social distancing guidelines?': 'Amount of Times Broken Social Distancing',
        'Who did you mainly live with during the majority of the quarantine period?': 'People Lived With DQ',
        'What was your main channel of communication with people who are not the people with whom you lived with?': 'Channel of Communication',
        'How often did you call your friends and family during the quarantine period?': 'Amount of Times Called Friends/Family',
        'Have you experienced cabin fever during the quarantine period?': 'Cabin Fever',
        'Exercising': 'Exercise Routines DQ',
        'How has quarantine affected your mental health?': 'Effects on Mental Health',
        'In what ways did quarantine affect your mental health?': 'Ways Quarantine Affected Mental Health',
        'What steps have you been taking to improving your mental health during quarantine': 'Steps Taken to Improve Mental Health DQ',
        'Do you currently suffer from a form of mental illness, and which one(s) do you suffer from?': 'Mental Illness',
        
        'Did you panic buy at the grocery store?': 'Panic Bought at Grocery Store',
        'How many rolls of toilet paper have you bought since the start of quarantine?': 'Rolls of Toilet Paper Bought',
        'Did you try cutting your own hair?': 'Cutting Own Hair',
        'How much money did you spend on Uber Eats/Equivalents?': 'Money Spent on Food Delivery Services',
        'How many days did you spend in pyjamas?': 'Days Spent in Pyjamas',
        'How many Dalgona Coffees did you make?': 'Dalgona Coffees Made',
        'Did you try making your own bread?': 'Made Own Bread',
        'Did you download any dating apps for the first time?': 'Dating App First Time Downloaders',
        'How often did you swipe on dating apps?': 'Time Spent Swiping on Dating Apps',
        'Did you use Tinder Passport / equivalents?': 'Use of Tinder Passport / Equivalents',
        'If you used dating apps before and during quarantine, did you receive more or less matches compared to the amount you usually get?': 'Changes in Match Rate Before and During Quarantine',
        'How often did you play video games?': 'Amount of Time Playing Video Games',
        'If you played Video Games, which ones did you play': 'Video Games Played',
        'Favourite TV Show / Movie / Web Series during quarantine': 'Favourite Entertainment Series',
    })
    return df


def clean_exam_difficulty(difficulty):
    # In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 211] AND OTHERS
    if(difficulty == '1 (Hardest)'):
        return 1
    elif(difficulty == '5 (Easiest)'):
        return 5
    else:
        return difficulty

def exam_difficulty_applymap(df):
    df[['In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 211]',
    "In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 223]",
    'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 261]',
    'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 283]',
    'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 285]'
    ]] = df[[
    'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 211]',
    "In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 223]",
    'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 261]',
    'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 283]',
    'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 285]'
    ]].applymap(clean_exam_difficulty)
    return df

def capitalize_string(word):
    if(word == 'US'):
        word = 'United States'
    elif(isinstance(word, float)):
        return word
    return word.title()

def capitalize_string_applymap(df):
    df[['City of Cancelled Job',
    'Country of Cancelled Job',
    'City of Job',
    'Country of Job',
    'Video Games Played',
    'Favourite Entertainment Series'
    ]] = df[[
    'City of Cancelled Job',
    'Country of Cancelled Job',
    'City of Job',
    'Country of Job',
    'Video Games Played',
    'Favourite Entertainment Series'
    ]].applymap(capitalize_string)
    return df

df_data_vis_std = pd.read_csv('')
df_data_vis_original = pd.read_csv('')
df_num_std = pd.read_csv('')
df_num_original = pd.read_csv('')



# exam_difficulty_columns = [
#     'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 211]',
#     'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 223]',
#     'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 261]',
#     'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 283]',
#     'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 285]'
# ]

# for columns in range (0, len(exam_difficulty_columns)):
#     df_data_vis_std = df_data_vis_std[exam_difficulty_columns[columns]].apply(clean_exam_difficulty)
#     df_data_vis_original = df_data_vis_original[exam_difficulty_columns[columns]].apply(clean_exam_difficulty)
#     df_num_std = df_num_std[exam_difficulty_columns[columns]].apply(clean_exam_difficulty)
#     df_num_original = df_num_original[exam_difficulty_columns[columns]].apply(clean_exam_difficulty)

df_data_vis_std = exam_difficulty_applymap(df_data_vis_std)
df_data_vis_original = exam_difficulty_applymap(df_data_vis_original)
df_num_std = exam_difficulty_applymap(df_num_std)
df_num_original = exam_difficulty_applymap(df_num_original)

df_data_vis_std = rename_column_headers(df_data_vis_std)
df_data_vis_original = rename_column_headers(df_data_vis_original)
df_num_std = rename_column_headers(df_num_std)
df_num_original = rename_column_headers(df_num_original)

# titles_to_capitalize = [
#     'City of Cancelled Job',
#     'Country of Cancelled Job',
#     'City of Job',
#     'County of Job',
#     'Video Games Played',
#     'Favourite Entertainment Series'
# ]

# for titles in range (0, len(titles_to_capitalize)):
#     df_data_vis_std[titles_to_capitalize[titles]].apply(capitalize_string)
#     df_data_vis_original[titles_to_capitalize[titles]].apply(capitalize_string)
#     df_num_std[titles_to_capitalize[titles]].apply(capitalize_string)
#     df_num_original[titles_to_capitalize[titles]].apply(capitalize_string)

df_data_vis_std.head()

df_data_vis_std = capitalize_string_applymap(df_data_vis_std)
df_data_vis_original = capitalize_string_applymap(df_data_vis_original)
df_num_std = capitalize_string_applymap(df_num_std)
df_num_original = capitalize_string_applymap(df_num_original)


path = r'...\csv\\'
df_data_vis_std.to_csv(path + 'data_vis_std.csv')
df_data_vis_original.to_csv(path + 'data_vis_text.csv')
df_num_std.to_csv(path + 'analysis_std.csv')
df_num_original.to_csv(path + 'analysis_text.csv')