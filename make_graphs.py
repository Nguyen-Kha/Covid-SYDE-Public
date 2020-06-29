from generate_graphs import *

df = pd.read_csv('')

### COLUMN NAME ARRAYS ###
# PIE Chart #
pie_columns_arr = [
    'Gender Identity',
    'Courses Taken',
    'Learning Style',
    'Courses CR/NCR-ed',
    'Had an Offer',
    'Had Cancelled Offer',
    'Country of Cancelled Job',
    'Field of Cancelled Job',
    'Industry of Cancelled Job',
    'Company Size of Cancelled Job',
    'Field of Job',
    'Country of Job',
    'Remote Job',
    'Size of Company',
    'Industry of Job',
    'Still Seeking Job',
    'Job Search Methods',
    'Amount of Times Broken Social Distancing',
    'Panic Bought at Grocery Store',
    'Cutting Own Hair',
    'Money Spent on Food Delivery Services',
    'Made Own Bread',
    'Dating App First Time Downloaders',
    'Time Spent Swiping on Dating Apps',
    'Use of Tinder Passport / Equivalents',
    'Changes in Match Rate Before and During Quarantine',
    'Amount of Time Playing Video Games',
    'Expenditures',
    'People Lived With DQ',
    'Channel of Communication',
    'Amount of Times Called Friends/Family'
]


### LOOPS TO EXPORT PNG ###
# PIE Chart #
for c in pie_columns_arr:
    create_pie(
        df,
        c,
        c + 'column',
        splice_required = False
    )


#################################
####   BQ DQ CHARTS #############

create_BQDQ_overlap(df, 'Study Habits BQ', 'Study Habits DQ', 'Habits', '% of Respondents', 'Study Habits', vertical=True, colour_rotation=['#fe5f55', '#087e8b'])
create_BQDQ_overlap(df, 'Side Projects BQ', 'Side Projects DQ', 'Amount of Side Projects', '% of Respondents', 'Side Projects', vertical=True, colour_rotation=['#fe5f55', '#087e8b'])
create_BQDQ_overlap(df, 'Class Attendance BQ', 'Class Attendance DQ', 'How Often the Respondent Attended Classes', '% of Respondents', 'Classes Attended', vertical=True, colour_rotation=['#fe5f55', '#087e8b'])
create_BQDQ_overlap(df, 'Days of Exercise per Week BQ', 'Days of Exercise per Week DQ', 'Days Exercised per Week', '% of Respondents', 'Days Exercised per Week', vertical=True, colour_rotation=['#fe5f55', '#087e8b'])
create_BQDQ_overlap(df, 'Average Stress Levels BQ', 'Average Stress Levels DQ', 'Stress Levels', '% of Respondents', 'Stress Levels', vertical=True, colour_rotation=['#fe5f55', '#087e8b'])