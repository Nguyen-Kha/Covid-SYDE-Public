import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import numpy as np
from collections import Counter

#####################################################
########   DEFAULT VALUES   #########################

def global_styling():
    styles = {
        'axes.titlesize' : #NUMBER,
        'axes.labelsize' : #NUMBER,
        'lines.linewidth' : #NUMBER,
        'lines.markersize' : #NUMBER,
        'xtick.labelsize' : #NUMBER,
        'ytick.labelsize' : #NUMBER,
        'legend.fontsize': #NUMBER,
    }
    plt.rcParams.update(styles)

# def apply_colours():



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
    x_bar_values: list = [],
): # TODO: INCOMPLETE - Steps, Ticks, Styles
    """
    vertical: True for vertical bar graph, False for horizontal graph
    """

    count = Counter()
#     if(splice_required):
#         column_values = splice_cells_with_commas(df, column_name)
#     else:
#         column_values = df[column_name]

#     for value in column_values:
    for value in df[column_name]:
        count[value] += 1
    
    df_temp = pd.DataFrame({'title': list(count.keys()), 'values': list(count.values())})
    if x_bar_values:
        df_temp.reindex(x_bar_values)

    fig, ax = plt.subplots(figsize = (11,9))
    
    if(vertical):
        ax.bar(
            x = df_temp['title'],
            height = df_temp['values'],
            align = 'center',
            zorder = 3
        )
        ax.set_xlabel(x_axis_label)
        ax.set_ylabel(y_axis_label)
        # plt.xticks()
    else:
        ax.barh(
            y = df_temp['title'],
            width = df_temp['values'],
            align = 'center',
            zorder = 3
        )
        ax.set_xlabel(x_axis_label)
        ax.set_ylabel(y_axis_label)
        # plt.yticks()

    plt.rcParams['axes.facecolor'] = '#E6E6E6'
    ax.grid(color='w', linestyle='solid', zorder=0)
    
    plt.title(title)

# DENSITY CHART - SHADED
def create_density(
    df,
    x_column_name,
    # y_column_name,
    x_axis_label,
    # y_axis_label,
    title,
    bar_values: list = [],
): # TODO: convert to column names list to overlay, style
    """
    """
    count = Counter()
    for value in df[x_column_name]:
        count[value] += 1
    
    df_temp = pd.DataFrame({'title': list(count.keys()), 'values': list(count.values())})
    if bar_values:
        df_temp.reindex(bar_values)

    plt.figure(figsize = (11,9))
    plt.title(label = title)
    sns.kdeplot(
        data = df_temp['title'],
        shade = True,
        color = "b",
        gridsize = 100,
        label = x_column_name
    )


# LINE CHART
def create_line(
    df,
    x_column_name,
    y_column_name,
    x_axis_label,
    y_axis_label,
    title
): #TODO: TEST
    df_temp = pd.DataFrame({x_column_name: df[x_column_name], y_column_name: df[y_column_name]})

    plt.figure(figsize = (11,9))
    sns.lineplot(
        x = x_column_name,
        y = y_column_name,
        data = df_temp
    )
    plt.title(label = title)


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

# # POINT PLOT
# def create_point(
#     df,
#     x_column_names: List = [],
#     x_axis_label,
#     y_axis_label,
#     hue_column_name,
# ):
#     """
#     """



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

def save_plot(fig, save_name):
    fig.savefig('../' + save_name)
    plt.close()

#####################################################
########   GENERATE GRAPHS   ########################

df = pd.read_csv('')
# create_pie(df, 'Learning Style', 'Learning Style')