import pandas as pd

def rename_column_headers(df):
    df.rename(columns={
        'If you lived off campus, when did you move out of Waterloo': 'Move-Out Date',
        'If you stayed in Waterloo for the majority of the quarantine period, why?': 'Reasons for Staying in Waterloo',
        'If you were not in Waterloo for the majority of the quarantine period, why?': 'Reasons for Leaving Waterloo',
        'How many courses were you taking?': 'Courses Taken',
        'What is your main learning style?': 'Learning Style',

    })


def clean_exam_difficulty(difficulty):
    # In terms of relative difficulty, rank the exams from hardest to easiest [SYDE 211] AND OTHERS
    if(difficulty == '1 (Hardest)'):
        return 1
    elif(difficulty == '5 (Easiest)'):
        return 5
    # elif(difficulty == 'N/A'):, or NaN, figure it out
    #     return # Whatever the mean for this is after we calculate it beforehand
    else:
        return difficulty

df_data_vis = pd.read_csv('')
df_num = pd.read_csv('')