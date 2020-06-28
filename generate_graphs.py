import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
from collections import Counter

#####################################################
########   DEFAULT VALUES   #########################

def global_styling():
    styles = {
        'axes.titlesize' : 20,
        'axes.labelsize' : 16,
        'lines.linewidth' : 20,
        'lines.markersize' : 20,
        'xtick.labelsize' : 14,
        'ytick.labelsize' : 14,
        'legend.fontsize': 16,
        'font.size': 18,
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
    bar_values: list = [],
    colour_rotation: list = ['blue'],
    x_increment = None,
    y_increment = None
): # TODO: INCOMPLETE - Steps, Ticks, Styles
    """
    vertical: True for vertical bar graph, False for horizontal graph
    """
    x_max_adjustment = 1
    y_max_adjustment = 1
    count = Counter()
#     if(splice_required):
#         column_values = splice_cells_with_commas(df, column_name)
#     else:
#         column_values = df[column_name]

#     for value in column_values:
    for value in df[column_name]:
        count[value] += 1
    
    df_temp = pd.DataFrame({'title': list(count.keys()), 'values': list(count.values())})
    if bar_values:
        df_temp.reindex(bar_values)

    fig, ax = plt.subplots(figsize = (11,9))
    
    if(not y_increment):
        y_increment = math.ceil(max(df_temp['values']) / 10)
    
    if(vertical):
        ax.bar(
            x = df_temp['title'],
            height = df_temp['values'],
            align = 'center',
            zorder = 3,
            color = colour_rotation
        )
        ax.set_xlabel(x_axis_label)
        ax.set_ylabel(y_axis_label)
#         ax.xaxis.set_ticks(np.arange(0, max(df_temp['title'])+x_max_adjustment, 1.0))
        ax.yaxis.set_ticks(np.arange(0, max(df_temp['values'])+y_max_adjustment, y_increment))
    else:
        ax.barh(
            y = df_temp['title'],
            width = df_temp['values'],
            align = 'center',
            zorder = 3,
            color = colour_rotation
        )
        ax.set_xlabel(x_axis_label)
        ax.set_ylabel(y_axis_label)
#         ax.xaxis.set_ticks(np.arange(min(df_temp['title']), max(df_temp['title'])+1, 1.0))
#         ax.yaxis.set_ticks(np.arange(min(df_temp['values']), max(df_temp['values'])+1, 5.0))
    
    plt.rcParams['axes.facecolor'] = '#E6E6E6'
    ax.grid(color='w', linestyle='solid', zorder=0)
    
    plt.title(title)
    global_styling()
    plt.savefig('.../test.png')
    plt.close()

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

    global_styling()
    plt.savefig('../test.png')
    plt.close()   

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
    global_styling()
    plt.savefig('../test.png')
    plt.close


# PIE CHART
def create_pie( 
    df,
    column_name,
    title,
    splice_required = False,
    colour_rotation: list = ['blue', 'red', 'green']
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

    global_styling()
    fig.savefig('.../test.png')
    plt.close()

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

    global_styling()
    plt.savefig('../test.png')
    plt.close()


def create_violin(
    df,
    column_x,
    column_y,    
    x_axis_label,
    y_axis_label,
    title,
    vertical: bool,
#     splice_required = False,
#     bar_values: list = [],
):

    fontsize = 10

#     orientation = ""
#     if (vertical):
#         orientation = "v"
#     else:
#         orientation = "h"
        
    fig, axes = plt.subplots()
    
    sns.violinplot(
        column_x,
        column_y, 
        data=df, 
        ax = axes,
        orient = "v"
    )

    axes.yaxis.grid(True)
    axes.set_xlabel(x_axis_label)
    axes.set_ylabel(y_axis_label)
    
    axes.set_title(title)
    global_styling()
    plt.savefig('.../test.png')
    plt.close()

def create_BQDQ_beside(
    df,
    column_name_BQ,
    column_name_DQ,
    x_axis_label,
    y_axis_label,
    title,
    vertical: bool,
    splice_required: bool = False,
    bar_values: list = [],
    colour_rotation: list = ['blue', 'red'],
):
    count1 = Counter()
    count2 = Counter()
    bar_width = 0.35
#     if(splice_required):
#         column_values = splice_cells_with_commas(df, column_name)
#     else:
#         column_values = df[column_name]

#     for value in column_values:
    for value in df[column_name_BQ]:
        count1[value] += 1
    for value in df[column_name_DQ]:
        count2[value] += 1
    
    df_temp1 = pd.DataFrame({'title': list(count1.keys()), 'values': list(count1.values())})
    df_temp2 = pd.DataFrame({'title': list(count2.keys()), 'values': list(count2.values())})
    if bar_values:
        df_temp.reindex(bar_values)

    fig, ax = plt.subplots(figsize = (11,9))
    
#     if(not y_increment):
#         y_increment = math.ceil(max(df_temp['values']) / 10)
    y_increment = 2
    
    if(vertical):
        ax.bar(
            x = df_temp1['title'] - bar_width/2,
            height = df_temp1['values'],
            align = 'center',
            zorder = 3,
            color = colour_rotation[0],
            label = column_name_BQ,
            alpha = 0.5,
            width = bar_width
        )
        ax.set_xlabel(x_axis_label)
        ax.set_ylabel(y_axis_label)
#         ax.xaxis.set_ticks(np.arange(0, max(df_temp['title'])+x_max_adjustment, 1.0))
        ax.yaxis.set_ticks(np.arange(0, max(df_temp1['values'])+1, y_increment))
    
        ax.bar(
            x = df_temp2['title'] + bar_width/2,
            height = df_temp2['values'],
            align = 'center',
            zorder = 3,
            color = colour_rotation[1],
            label = column_name_DQ,
            alpha = 0.5,
            width = bar_width
        )
        ax.set_xlabel(x_axis_label)
        ax.set_ylabel(y_axis_label)
#         ax.xaxis.set_ticks(np.arange(0, max(df_temp['title'])+x_max_adjustment, 1.0))
        ax.yaxis.set_ticks(np.arange(0, max(df_temp2['values'])+1, y_increment))
    else:
        ax.barh(
            y = df_temp['title'],
            width = df_temp['values'],
            align = 'center',
            zorder = 3,
            color = colour_rotation[0]
        )
        ax.set_xlabel(x_axis_label)
        ax.set_ylabel(y_axis_label)
#         ax.xaxis.set_ticks(np.arange(min(df_temp['title']), max(df_temp['title'])+1, 1.0))
#         ax.yaxis.set_ticks(np.arange(min(df_temp['values']), max(df_temp['values'])+1, 5.0))
    
    plt.rcParams['axes.facecolor'] = '#E6E6E6'
    ax.grid(color='w', linestyle='solid', zorder=0)
    plt.legend(title="Legend")
    plt.title(title)
    global_styling()
    plt.savefig('.../test.png')
    plt.close()

def create_BQDQ_overlap(
    df,
    column_name_BQ,
    column_name_DQ,
    x_axis_label,
    y_axis_label,
    title,
    vertical: bool,
    splice_required: bool = False,
    bar_values: list = [],
    colour_rotation: list = ['blue', 'red'],
):
    count1 = Counter()
    count2 = Counter()
#     if(splice_required):
#         column_values = splice_cells_with_commas(df, column_name)
#     else:
#         column_values = df[column_name]

#     for value in column_values:
    for value in df[column_name_BQ]:
        count1[value] += 1
    for value in df[column_name_DQ]:
        count2[value] += 1
    
    df_temp1 = pd.DataFrame({'title': list(count1.keys()), 'values': list(count1.values())})
    df_temp2 = pd.DataFrame({'title': list(count2.keys()), 'values': list(count2.values())})
    if bar_values:
        df_temp.reindex(bar_values)

    fig, ax = plt.subplots(figsize = (11,9))
    
#     if(not y_increment):
#         y_increment = math.ceil(max(df_temp['values']) / 10)
    y_increment = 2
    
    if(vertical):
        ax.bar(
            x = df_temp1['title'],
            height = df_temp1['values'],
            align = 'center',
            zorder = 3,
            color = colour_rotation[0],
            label = column_name_BQ,
            alpha = 0.5
        )
        ax.set_xlabel(x_axis_label)
        ax.set_ylabel(y_axis_label)
#         ax.xaxis.set_ticks(np.arange(0, max(df_temp['title'])+x_max_adjustment, 1.0))
        ax.yaxis.set_ticks(np.arange(0, max(df_temp1['values'])+1, y_increment))
    
        ax.bar(
            x = df_temp2['title'],
            height = df_temp2['values'],
            align = 'center',
            zorder = 3,
            color = colour_rotation[1],
            label = column_name_DQ,
            alpha = 0.5
        )
        ax.set_xlabel(x_axis_label)
        ax.set_ylabel(y_axis_label)
#         ax.xaxis.set_ticks(np.arange(0, max(df_temp['title'])+x_max_adjustment, 1.0))
        ax.yaxis.set_ticks(np.arange(0, max(df_temp2['values'])+1, y_increment))
    else:
        ax.barh(
            y = df_temp['title'],
            width = df_temp['values'],
            align = 'center',
            zorder = 3,
            color = colour_rotation[0]
        )
        ax.set_xlabel(x_axis_label)
        ax.set_ylabel(y_axis_label)
#         ax.xaxis.set_ticks(np.arange(min(df_temp['title']), max(df_temp['title'])+1, 1.0))
#         ax.yaxis.set_ticks(np.arange(min(df_temp['values']), max(df_temp['values'])+1, 5.0))
    
    plt.rcParams['axes.facecolor'] = '#E6E6E6'
    ax.grid(color='w', linestyle='solid', zorder=0)
    plt.legend(title="Legend")
    plt.title(title)
    global_styling()
    plt.savefig('.../test.png')
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

def save_plot(fig):
    fig.savefig('../test')
    plt.close()

#####################################################
########   GENERATE GRAPHS   ########################

df = pd.read_csv('')
# create_pie(df, 'Learning Style', 'Learning Style')