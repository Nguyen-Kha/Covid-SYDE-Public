import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
from collections import Counter

#####################################################
########   GRAPH FUNCTIONS   ########################

# BAR CHART
def create_bar(
    df,
    column_name,
    x_axis_label,
    y_axis_label,
    title,
    vertical: bool,
    splice_required = False,
    bar_values: list = [],
): # TODO: INCOMPLETE - Steps, Ticks, Styles
    """
    vertical: True for vertical bar graph, False for horizontal graph
    """

    count = Counter()
    if(splice_required):
        column_values = splice_cells_with_commas(df, column_name)
    else:
        column_values = df[column_name]

    for value in column_values:
        count[value] += 1
    
    df_temp = pd.DataFrame({'title': list(count.keys()), 'values': list(count.values())})
    if bar_values:
        df_temp.reindex(bar_values)

    plt.figure(figsize = (11,9))

    if(vertical):
        plt.bar(
            x = df_temp['title'],
            height = df_temp['values'],
            align = 'center',
        )
        plt.xlabel(x_axis_label)
        plt.ylabel(y_axis_label)
        # plt.xticks()
    else:
        plt.barh(
            y = df_temp['title'],
            width = df_temp['values'],
            align = 'center',
        )
        plt.xlabel(x_axis_label)
        plt.ylabel(y_axis_label)
        # plt.yticks()
    
    plt.title(title)
    plt.savefig('.../test.png')
    plt.close()

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

# SCATTER PLOT
def create_scatter(
    df,
    x_column_name,
    y_column_name,
    x_axis_label,
    y_axis_label,
    title,
    x_axis_values: list = []
): # TODO: Figure out a way to account for sizes of dots, add styles, adjust scales
    df_temp = pd.DataFrame({x_column_name: df[x_column_name], y_column_name: df[y_column_name]})
    if(x_axis_values):
        df_temp = df_temp.sort_values(by=[x_axis_values])
    else:
        df_temp = df_temp.sort_values(by=[x_column_name], ascending=True)
    
    plt.figure(figsize = (11,9))
    plt.scatter(
        x = df_temp[x_column_name],
        y = df_temp[y_column_name],
    )
    plt.title(label = title)
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.savefig('../test.png')
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