import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
from collections import Counter

#####################################################
########   GRAPH FUNCTIONS   ########################

# PIE CHART
def create_pie(
    df,
    column_name,
    title
):
    count = Counter()
    for value in df[column_name]:
        count[value] += 1
    
    df_temp = pd.DataFrame({'title': list(count.keys()), 'values': list(count.values())})
    df_temp = df_temp.sort_values(by=['values'], ascending = False)
    
    fig = plt.figure(figsize = (11,9))
    plt.pie(
        x = df_temp['values'],
        labels = df_temp['title'],
        autopct = '%1.1f%%',
        startangle = 90,
        labeldistance = None,
       )
    
    plt.title(label = title)
    plt.legend(df_temp['title'], title='Legend')
    plt.axis('equal')

    fig.savefig('.../test.png')


#####################################################
########   GENERATE GRAPHS   ########################

df = pd.read_csv('')
create_pie(df, 'Learning Style', 'Learning Style')