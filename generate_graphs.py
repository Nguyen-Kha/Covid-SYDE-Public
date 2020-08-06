import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
from collections import Counter
from wordcloud import WordCloud

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
    df_a,
    column_name,
    title_label,
    values_label,
    title,
    vertical: bool,
    title_increment = None,
    values_increment = None,
    values_max = None,
    splice_required: bool = False,
    labels: list = [],
    colours_list = [],
    convert_to_string = False,
    one_seven_scale = False,
):
    df = pd.DataFrame()
    if (not colours_list):
        colours = sns.color_palette('muted')
    else:
        colours = colours_list
    
    count = Counter()
    
    if(df_a[column_name].isnull().values.any()):
        df[column_name] = df_a[column_name].dropna(axis=0)
    else:
        df = df_a
    
    if(convert_to_string):
        df[column_name] = df[column_name].astype(str)
        
    ######################
    ## Count the amount of instances of each occurence in the dataset
    if(splice_required):
        column_values = splice_cells_with_commas(df, column_name)
        for i in column_values:
            count[i] += 1
            
    else:
#         column_values = df[column_name]
        for value in df[column_name]:
            count[value] += 1 
    
    if(one_seven_scale):
        count = {str(int(k)):int(v) for k,v in count.items()}
        
     ######################
    ## Put the counted values into a new dataframe
    if(labels):
        title_temp = list(count.keys())
        values_temp = list(count.values())
        dictionary = {title_temp[i] : values_temp[i] for i in range(0, len(title_temp))}

        df_temp = pd.DataFrame()
        df_temp['title'] = labels
        df_temp['values'] = 0

        for key, value in dictionary.items():
            for i in range(0, len(df_temp)):
                if(df_temp['title'][i] == key):
                    df_temp['values'][i] = value
    
    else:
        df_temp = pd.DataFrame({'title': list(count.keys()), 'values': list(count.values())})
    
    ######################
    ## Convert amount of people responded into percentages
    number_of_answers = len(df.index)
    df_temp['values'] = df_temp['values'] / number_of_answers * 100
    
    ###################
    ## Set axis interval increments
    if(not title_increment):
        title_increment = 1
    
    if(not values_max):
        values_max = max(df_temp['values'])
        
    if(not values_increment):
        values_increment = math.ceil(values_max / 10)
        
    x = np.arange(len(labels))  # the label locations

    fig, ax = plt.subplots(figsize = (11,9))
    
    if(labels):
        if(vertical):
            ax.bar(
                x = x,
                height = df_temp['values'].values,
                align = 'center',
                zorder = 3,
#                 color = colours_list[0],
                color = colours,
                label = column_name,
                alpha = 0.75,
            )
            ax.set_xlabel(title_label)
            ax.set_ylabel(values_label)
            ax.set_xticks(x)
            ax.set_xticklabels(labels)
            ax.yaxis.set_ticks(np.arange(0, values_max, values_increment))

        else:
            ax.barh(
                # y = df_temp['title'],
                y = x,
                # width = df_temp['values'],
                width = df_temp['values'],
                align = 'center',
                zorder = 3,
                color = colours,
                label = column_name,
                alpha = 0.75,
            )
            ax.set_xlabel(values_label)
            ax.set_ylabel(title_label)
            ax.set_yticks(x)
            ax.set_yticklabels(labels)
            ax.xaxis.set_ticks(np.arange(0, values_max, values_increment))
    
    else: 
        if(vertical):
            ax.bar(
                x = df_temp['title'],
                height = df_temp['values'],
                align = 'center',
                zorder = 3,
                color = colours,
                label = column_name,
                alpha = 0.75,
            )
            ax.set_xlabel(title_label)
            ax.set_ylabel(values_label)
            ax.yaxis.set_ticks(np.arange(0, values_max, values_increment))
#             ax.xaxis.set_ticks(np.arange(0, title_max, title_increment))

        else:
            ax.barh(
                y = df_temp['title'],
                width = df_temp['values'],
                align = 'center',
                zorder = 3,
                color = colours,
                label = column_name,
                alpha = 0.75,

            )
            ax.set_xlabel(values_label)
            ax.set_ylabel(title_label)
            ax.xaxis.set_ticks(np.arange(0, values_max, values_increment))
#             ax.yaxis.set_ticks(np.arange(0, title_max, title_increment))       

    
    plt.rcParams['axes.facecolor'] = '#F0F0F0'
    ax.grid(color='w', linestyle='solid', zorder=0)
    plt.legend(title="Legend", facecolor='white')
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

def create_BQDQ_beside_new2(
    df,
    column_name_BQ,
    column_name_DQ,
    title_label,
    values_label,
    title,
    vertical: bool,
    title_increment = None,
    values_increment = None,
    splice_required: bool = False,
    labels: list = [],
    colours_list = ['#4878d0', '#d65f5f'],
    convert_to_string = False
):
    if (not colours_list):
        colours = sns.color_palette('muted')
    else:
        colours = colours_list
    
    count1 = Counter()
    count2 = Counter()
    bar_width = 0.35
    
    if(convert_to_string):
        df[column_name_BQ] = df[column_name_BQ].astype(str)
        df[column_name_DQ] = df[column_name_DQ].astype(str)
        
#     if(splice_required):
#         column_values = splice_cells_with_commas(df, column_name)
#     else:
#         column_values = df[column_name]

#     for value in column_values:
    ######################
    ## Count the amount of instances of each occurence in the dataset
    for value in df[column_name_BQ]:
        count1[value] += 1
    for value in df[column_name_DQ]:
        count2[value] += 1
        
     ######################
    ## Put the counted values into a new dataframe
    if(labels):
        title_temp_BQ = list(count1.keys())
        title_temp_DQ = list(count2.keys())
        values_temp_BQ = list(count1.values())
        values_temp_DQ = list(count2.values())
        dictionary_BQ = {title_temp_BQ[i] : values_temp_BQ[i] for i in range(0, len(title_temp_BQ))}
        dictionary_DQ = {title_temp_DQ[i] : values_temp_DQ[i] for i in range(0, len(title_temp_DQ))}

        df_temp1 = pd.DataFrame()
        df_temp1['title'] = labels
        df_temp1['values'] = 0
        
        df_temp2 = pd.DataFrame()
        df_temp2['title'] = labels
        df_temp2['values'] = 0

        for key, value in dictionary_BQ.items():
            for i in range(0, len(df_temp1)):
                if(df_temp1['title'][i] == key):
                    df_temp1['values'][i] = value
                    
        for key, value in dictionary_DQ.items():
            for i in range(0, len(df_temp2)):
                if(df_temp2['title'][i] == key):
                    df_temp2['values'][i] = value
    
    else:
        df_temp1 = pd.DataFrame({'title': list(count1.keys()), 'values': list(count1.values())})
        df_temp2 = pd.DataFrame({'title': list(count2.keys()), 'values': list(count2.values())})
    
    ######################
    ## Convert amount of people responded into percentages
    number_of_answers1 = len(df_temp1.index)
    number_of_answers2 = len(df_temp2.index)
    df_temp1['values'] = df_temp1['values'] / number_of_answers1 * 100
    df_temp2['values'] = df_temp2['values'] / number_of_answers2 * 100
    
    if(max(df_temp1['values']) < max(df_temp2['values'])):
        values_max = max(df_temp2['values']) +1
    else:
        values_max = max(df_temp1['values']) +1
    
    ###################
    ## Set axis interval increments
    if(not title_increment):
        title_increment = 1
        
    if(not values_increment):
        values_increment = math.ceil(values_max / 10)
        
    x = np.arange(len(labels))  # the label locations

    fig, ax = plt.subplots(figsize = (11,9))
    
    if(labels):
        if(vertical):
            ax.bar(
                x = x - bar_width/2,
                height = df_temp1['values'].values,
                align = 'center',
                zorder = 3,
                color = colours_list[0],
                label = column_name_BQ,
                alpha = 0.75,
                width = bar_width
            )
            ax.set_xlabel(title_label)
            ax.set_ylabel(values_label)
            ax.set_xticks(x)
            ax.set_xticklabels(labels)
            ax.yaxis.set_ticks(np.arange(0, values_max, values_increment))

            ax.bar(
                x = x + bar_width/2,
                height = df_temp2['values'].values,
                align = 'center',
                zorder = 3,
                color = colours_list[1],
                label = column_name_DQ,
                alpha = 0.75,
                width = bar_width
            )

        else:
            ax.barh(
                # y = df_temp['title'],
                y = x - bar_width/2,
                # width = df_temp['values'],
                width = df_temp1['values'],
                align = 'center',
                zorder = 3,
                color = colours_list[0],
                label = column_name_BQ,
                alpha = 0.75,
                height = bar_width
            )
            ax.set_xlabel(values_label)
            ax.set_ylabel(title_label)
            ax.set_yticks(x)
            ax.set_yticklabels(labels)
            ax.xaxis.set_ticks(np.arange(0, values_max, values_increment))

            ax.barh(
                # y = df_temp['title'],
                y = x + bar_width/2,
                # width = df_temp['values'],
                width = df_temp2['values'],
                align = 'center',
                zorder = 3,
                color = colours_list[1],
                label = column_name_DQ,
                alpha = 0.75,
                height = bar_width
            )
    
    else:
        if(max(df_temp1['title']) < max(df_temp2['title'])):
            title_max = max(df_temp2['title']) +1
        else:
            title_max = max(df_temp1['title']) +1
            
        if(vertical):
            ax.bar(
                x = df_temp1['title'] - bar_width/2,
                height = df_temp1['values'],
                align = 'center',
                zorder = 3,
                color = colours_list[0],
                label = column_name_BQ,
                alpha = 0.75,
                width = bar_width
            )
            ax.set_xlabel(title_label)
            ax.set_ylabel(values_label)
            ax.yaxis.set_ticks(np.arange(0, values_max, values_increment))
            ax.xaxis.set_ticks(np.arange(0, title_max, title_increment))

            ax.bar(
                x = df_temp2['title'] + bar_width/2,
                height = df_temp2['values'],
                align = 'center',
                zorder = 3,
                color = colours_list[1],
                label = column_name_DQ,
                alpha = 0.75,
                width = bar_width
            )

        else:
            ax.barh(
                y = df_temp1['title'] - bar_width/2,
                width = df_temp1['values'],
                align = 'center',
                zorder = 3,
                color = colours_list[0],
                label = column_name_BQ,
                alpha = 0.75,
                height = bar_width
            )
            ax.set_xlabel(values_label)
            ax.set_ylabel(title_label)
            ax.xaxis.set_ticks(np.arange(0, values_max, values_increment))
            ax.yaxis.set_ticks(np.arange(0, title_max, title_increment))       

            ax.barh(
                y = df_temp2['title'] + bar_width/2,
                width = df_temp2['values'],
                align = 'center',
                zorder = 3,
                color = colours_list[1],
                label = column_name_BQ,
                alpha = 0.75,
                height = bar_width
            )
    
    plt.rcParams['axes.facecolor'] = '#F0F0F0'
    ax.grid(color='w', linestyle='solid', zorder=0)
    plt.legend(title="Legend", facecolor='white')
    plt.title(title)
    global_styling()
    plt.savefig('.../test.png')
    plt.close()

def create_wordcloud(
    df,
    column_name,
    save_name
):
    
    if(df[column_name].isnull().values.any()):
        df[column_name] = df[column_name].dropna(axis=0)
    
    count = Counter()
    column_values = splice_cells_with_commas(df, column_name)
    for i in column_values:
        count[i] += 1
    
    wordcloud = WordCloud(width = 600, height = 400, background_color = 'white').generate_from_frequencies(count)
    plt.imshow(wordcloud, interpolation = 'bilinear')
    plt.axis("off")
    wordcloud.to_file('../' + save_name + '_wordmap.png')

#####################################################
########   HELPER FUNCTIONS   #######################

def splice_cells_with_commas(df, column_name): # TODO: TEST
    """
    RETURNS: ARRAY of values to be counted with COUNTER
    # TODO: Do some dictionary work instead
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