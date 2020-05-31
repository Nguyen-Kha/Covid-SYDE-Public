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
    title,
    splice_required = False
): # TODO: TEST
    count = Counter()
    if(splice_required):
        column_values = splice_cells_with_commas(df, column_name)
    else:
        column_values = df[column_name]

    # Change: Append cells to an array. arrays with arrays in them, splice it
    for value in column_values:
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
    plt.close()

#####################################################
########   HELPER FUNCTIONS   #######################

def splice_cells_with_commas(df, column_name): # TODO: TEST
    """
    RETURNS: ARRAY of values to be counted with COUNTER
    """
    spliced_array = []
    for item in df[column_name]:
        if(type(item) != float):
            potential_list = item.split(', ')
            for single in potential_list:
                spliced_array.append(single)
    
    return spliced_array

#####################################################
########   GENERATE GRAPHS   ########################

df = pd.read_csv('')
# create_pie(df, 'Learning Style', 'Learning Style')