import pandas as pd

def rename_column_headers(df):
    df.rename(columns = {
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

        'Difficulty of each online exam compared to an in class exam': '',
        'How long did you take to write each timed exam?': '',
        'How long did the SYDE 261 exam take you to complete?': '',
        'How long did the SYDE 285 Written portion take you to complete?': '',
        'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 211]': '',
        'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 223]': '',
        'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 261]': '',
        'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 283]': '',
        'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 285]': '',
        'Amount of hours spent studying for each exam [SYDE 211]': '',
        'Amount of hours spent studying for each exam [SYDE 223]': '',
        'Amount of hours spent studying for each exam [SYDE 261]': '',
        'Amount of hours spent studying for each exam [SYDE 283]': '',
        'Amount of hours spent studying for each exam [SYDE 285]': '',
        'Amount of hours spent studying for each exam [Electives]': '',
        'Which marks did you walk into each exam with? [SYDE 211]': '',
        'Which marks did you walk into each exam with? [SYDE 223]': '',
        'Which marks did you walk into each exam with? [SYDE 261]': '',
        'Which marks did you walk into each exam with? [SYDE 283]': '',
        'Which marks did you walk into each exam with? [SYDE 285]': '',
        'Stress level during a timed exam': '',
        'Rank your Term Average from Lowest (1) to Highest (3)  [1A]': '',
        'Rank your Term Average from Lowest (1) to Highest (3)  [1B]': '',
        'Rank your Term Average from Lowest (1) to Highest (3)  [2A]': '',
        'How did the quarantine effect your motivation to study? ': '',
        'How did quarantine affect your work ethic?': '',
        'How many hours did you spend on the following assignments? [SYDE 223 PE 2]': '',
        'How many hours did you spend on the following assignments? [SYDE 261 Project 2]': '',
        'How many hours did you spend on the following assignments? [SYDE 261 Project 3]': '',
        'How many hours did you spend on the following assignments? [SYDE 285 Term Project]': '',
        'Ease of learning online (comparing to in-class)': '',
        'How many courses do you plan on CR/NCR-ing?': '',
        'Main Methods of Studying': '',
        
        'What type of roles were you going for?': '',
        'How many applications did you send out?': '',
        'How many interviews did you receive?': '',
        'Was there a large amount of postings for your ideal positions on WaterlooWorks?': '',
        'At any point in the term, did you have an offer for a co-op job?': '',
        'At any point in the term, did you receive an offer that got cancelled?': '',

        'Which field was this cancelled job in?': '',
        'In which city would your job have been located in?': '',
        'In which country would your job have been located in?': '',
        'What would have been the size of your company': '',
        'What is the net worth of that company?': '',
        'Which Industry best describes the company you would have worked for?': '',
        'When was your job cancelled?': '',
        'Did you end up finding a job as of May 1st?': '',

        'Which field was this job in?': '',
        'In which city is your job located?': '',
        'In which country is your job located?': '',
        'Is your job currently remote?': '',
        'What is the size of your company': '',
        'What is the net worth of your company?': '',
        'Which Industry best describes the company you are for?': '',
        'When did you get your job?': '',

        'Are you still actively seeking a co-op position?': '',
        'How have you been looking for co-op jobs?': '',
        'How are you planning on spending your spring term?': '',

        'How worried are you on your current financial situation during this quarantine period?': '',
        'Have you been negatively affected financially by COVID-19 in any way?': '',
        'What are your main financial concerns of COVID-19?': '',
        'Do you qualify for CESB / CERB?': '',
        'Did you apply for CESB / CERB?': '',
        'Have your spending habits increased or decreased?': '',
        'Which of the following items did you spend most of your money on during the quarantine period? Choose 3.': '',
        'How do you plan on financing your 2B term?': '',

        'How many times did you break social distancing guidelines?': '',
        'Who did you mainly live with during the majority of the quarantine period?': '',
        'What was your main channel of communication with people who are not the people with whom you lived with?': '',
        'How often did you call your friends and family during the quarantine period?': '',
        'Have you experienced cabin fever during the quarantine period?': '',
        'Exercising': '',
        'How has quarantine affected your mental health?': '',
        'In what ways did quarantine affect your mental health?': '',
        'What steps have you been taking to improving your mental health during quarantine': '',
        'Do you currently suffer from a form of mental illness, and which one(s) do you suffer from?': '',
        
        'Did you panic buy at the grocery store?': '',
        'How many rolls of toilet paper have you bought since the start of quarantine?': '',
        'Did you try cutting your own hair?': '',
        'How much money did you spend on Uber Eats/Equivalents?': '',
        'How many days did you spend in pyjamas?': '',
        'How many Dalgona Coffees did you make?': '',
        'Did you try making your own bread?': '',
        'Did you download any dating apps for the first time?': '',
        'How often did you swipe on dating apps?': '',
        'Did you use Tinder Passport / equivalents?': '',
        'If you used dating apps before and during quarantine, did you receive more or less matches compared to the amount you usually get?': '',
        'How often did you play video games?': '',
        'If you played Video Games, which ones did you play': '',
        'Favourite TV Show / Movie / Web Series during quarantine': '',

    })


def clean_exam_difficulty(difficulty):
    # In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 211] AND OTHERS
    if(difficulty == '1 (Hardest)'):
        return 1
    elif(difficulty == '5 (Easiest)'):
        return 5
    else:
        return difficulty

df_data_vis = pd.read_csv('')
df_num = pd.read_csv('')

exam_difficulty_columns = [
    'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 211]',
    'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 223]',
    'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 261]',
    'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 283]',
    'In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 285]'
]

for columns in exam_difficulty_columns:
    df_data_vis[exam_difficulty_columns[columns]].apply(clean_exam_difficulty)
    df_num[exam_difficulty_columns[columns]].apply(clean_exam_difficulty)
