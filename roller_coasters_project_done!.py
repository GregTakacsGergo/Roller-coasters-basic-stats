# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:08:10 2020

@author: esgorath
"""
import pandas as pd
from matplotlib import pyplot as plt

wooden_roller_coaster = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
steel_roller_coaster = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
together = [wooden_roller_coaster, steel_roller_coaster]
concat_roller_coaster = pd.concat(together)
#print(concat_roller_coaster.head(10))

#lets see if there is any name overlap btwn wooden, and steel rollers...
duplicates = set(wooden_roller_coaster.Name).intersection(steel_roller_coaster.Name)
#print(duplicates)
#since I can see only one match 'Goliath', it's unnecesary to use more than a single parameter in here, 
#it's unnecesary to tell except 'Goliath' which DataFrame do we use (wooden_roller_coaster, OR, steel_roller_coaster) 
# function to plot rankings over time for 1 roller coaster
def roller_coaster_ranking(roller_coaster_name):
  material = ''
  wooden_roller_coaster_LIST = wooden_roller_coaster.Name.values.tolist()
  steel_roller_coaster_LIST = steel_roller_coaster.Name.values.tolist()
  if roller_coaster_name in wooden_roller_coaster_LIST:
    material = 'Wooden'
  elif roller_coaster_name in steel_roller_coaster_LIST:
    material = 'Steel'    
  rows_we_need = concat_roller_coaster[concat_roller_coaster.Name == roller_coaster_name]
  years = rows_we_need['Year of Rank']
  ranks = rows_we_need['Rank']
  plt.figure(figsize=(12,10))
  plt.plot(range(len(years)), ranks, marker='o', color='red')  
  plt.ylabel('Ranks')
  plt.xlabel('Years')
  plt.title(roller_coaster_name +' ranking over time' + ' (' + material + ')')
  plt.show()  
  ax = plt.subplot()
  ax.set_xticks(range(len(years)))
  ax.set_xticklabels(years)
  ax.invert_yaxis()

  plt.savefig('C:/Users/esgorath/.spyder-py3/Roller Coaster project/PLOTS/El Toro in years.png')
  
#roller_coaster_ranking("El Toro")
plt.clf()

# write function to plot rankings over time for 2 roller coasters here:
def TWO_roller_coasters_ranking(roller_coaster_name1,roller_coaster_name2):
  material1 = ''
  material2 = ''
  wooden_roller_coaster_LIST = wooden_roller_coaster.Name.values.tolist()
  steel_roller_coaster_LIST = steel_roller_coaster.Name.values.tolist()
  if roller_coaster_name1 in wooden_roller_coaster_LIST:
    material1 = 'Wooden'
  elif roller_coaster_name1 in steel_roller_coaster_LIST:
    material1 = 'Steel'    
  if roller_coaster_name2 in wooden_roller_coaster_LIST:
    material2 = 'Wooden'
  elif roller_coaster_name2 in steel_roller_coaster_LIST:
    material2 = 'Steel'  
  rows_we_need1 = concat_roller_coaster[concat_roller_coaster.Name == roller_coaster_name1]
  years1 = rows_we_need1['Year of Rank']
  ranks1 = rows_we_need1['Rank']
  rows_we_need2 = concat_roller_coaster[concat_roller_coaster.Name == roller_coaster_name2]
  years2 = rows_we_need2['Year of Rank']
  ranks2 = rows_we_need2['Rank']
  plt.figure(figsize=(10,8))
  ax = plt.subplot()
  plt.plot(range(len(years1)), ranks1, marker='o', color='red', label=roller_coaster_name1)
  plt.plot(range(len(years2)), ranks2, marker='o', color='blue', label=roller_coaster_name2)
  ax.set_xticks(range(len(years1)))
  ax.set_xticklabels(years1)
  ax.invert_yaxis()
  plt.ylabel('Ranks')
  plt.xlabel('Years')
  plt.legend(loc='best')
  plt.title(roller_coaster_name1 + ' (' + material1 + ')'+ ' and ' + roller_coaster_name2 + ' (' + material2 + ')' + ' ranking over time' )
  plt.savefig('C:/Users/esgorath/.spyder-py3/Roller Coaster project/El Toro, Boulder Dash in years.png')
#TWO_roller_coasters_ranking("El Toro", "Boulder Dash")
plt.clf()
# write function to plot top n rankings over time here:
def plot_top_n(material, n):
  if material == 'wood':
    top_n_rankings = wooden_roller_coaster.head(n)   
    for name_i in list(top_n_rankings.Name):
      row_we_need = wooden_roller_coaster[wooden_roller_coaster.Name == name_i]
      plt.plot(row_we_need['Year of Rank'], row_we_need.Rank, marker='o', label=name_i)
    ax = plt.subplot()
    ax.invert_yaxis()
    plt.ylabel('Ranks')
    plt.xlabel('Years')
    plt.legend(loc='best') 
    plt.title('Top ' + str(n) + ' wooden roller coasters over time')
  plt.savefig('C:/Users/esgorath/.spyder-py3/Roller Coaster project/Top n wooden roller coasters.png')    
 
  if material == 'steel':
    top_n_rankings = steel_roller_coaster.head(n)   
    for name_i in list(top_n_rankings.Name):
      row_we_need = steel_roller_coaster[steel_roller_coaster.Name == name_i]
      plt.plot(row_we_need['Year of Rank'], row_we_need.Rank, marker='o', label=name_i)
    ax = plt.subplot()
    ax.invert_yaxis()
    plt.ylabel('Ranks')
    plt.xlabel('Years')
    plt.legend(loc='best') 
    plt.title('Top ' + str(n) + ' steel roller coasters over time')
  plt.savefig('C:/Users/esgorath/.spyder-py3/Roller Coaster project/Top n steel roller coasters.png')

#plot_top_n('steel', 8)
plt.clf()

# load roller coaster data here:
roller_coasters = pd.read_csv('roller_coasters.csv')
row_count = roller_coasters.shape[0] 
roller_coasters.insert(0, 'Index', [i for i in range(row_count)]) 

# write function to plot histogram of column values here:
def any_column_roller_coasters_plot(column):
  if column == 'material_type':
    dataframe_we_need = roller_coasters.groupby(column)['Index'].nunique().reset_index()
    sorted_dataframe_we_need = dataframe_we_need.sort_values(by=['Index'], ascending=False)
    x = sorted_dataframe_we_need['material_type'].tolist()
    print(x)
    y = sorted_dataframe_we_need['Index'].tolist()
    print(y)  
    fig, ax = plt.subplots()
    plt.bar(x, y, width=0.4)
    plt.title('Organize by ' + column.upper())
    plt.xlabel(column.upper())
    plt.ylabel('Nr. of roller coasters')
    ax.set_xticks(range(len(x)))
    ax.set_xticklabels(x, rotation=45, ha='right')    
    plt.savefig('C:/Users/esgorath/.spyder-py3/Roller Coaster project/PLOTS/{}'.format(column + '_historgam'))
    plt.show()
  elif column == 'seating_type':
    dataframe_we_need = roller_coasters.groupby(column)['Index'].nunique().reset_index()
    sorted_dataframe_we_need = dataframe_we_need.sort_values(by=['Index'], ascending=False)
    x = sorted_dataframe_we_need['seating_type'].tolist()
    print(x)
    y = sorted_dataframe_we_need['Index'].tolist()
    print(dataframe_we_need)
    plt.bar(x, y, width=0.4)
    plt.title('Organize by ' + column.upper())
    plt.xlabel(column.upper())
    plt.ylabel('Nr. of roller coasters')
    ax = plt.subplot()
    ax.set_xticks(range(len(x)))
    ax.set_xticklabels(x, rotation=45, ha='right')
    plt.savefig('C:/Users/esgorath/.spyder-py3/Roller Coaster project/PLOTS/{}'.format(column + '_historgam'))
 
  elif column == 'manufacturer':
    dataframe_we_need = roller_coasters.groupby(column)['Index'].nunique().reset_index()
    sorted_dataframe_we_need = dataframe_we_need.sort_values(by=['Index'], ascending=False)
    x = sorted_dataframe_we_need['manufacturer'].tolist()
    print(x)
    y = sorted_dataframe_we_need['Index'].tolist()
    print(dataframe_we_need)
    plt.bar(x, y, width=0.4)
    plt.title('Organize by ' + column.upper())
    plt.xlabel(column.upper())
    plt.ylabel('Nr. of roller coasters')
    ax = plt.subplot()
    ax.set_xticks(range(len(x)))
    ax.set_xticklabels(x, rotation=45, ha='right')
    plt.savefig('C:/Users/esgorath/.spyder-py3/Roller Coaster project/PLOTS/{}'.format(column + '_historgam'))
  
  elif column == 'park':
    dataframe_we_need = roller_coasters.groupby(column)['Index'].nunique().reset_index()
    sorted_dataframe_we_need = dataframe_we_need.sort_values(by=['Index'], ascending=False)
    x_all = sorted_dataframe_we_need['park'].tolist()
    x = x_all[0:25]
    #print(x)
    y_all = sorted_dataframe_we_need['Index'].tolist()
    y = y_all[0:25]
    #print(dataframe_we_need)
    plt.figure(figsize=(12,12))
    plt.bar(x, y, width=0.4)
    plt.title('Organize by ' + column.upper())
    plt.xlabel(column.upper())
    plt.ylabel('Nr. of roller coasters')
    ax = plt.subplot()
    ax.set_xticks(range(len(x)))
    ax.set_xticklabels(x, rotation=45, ha="right")
    plt.savefig('C:/Users/esgorath/.spyder-py3/Roller Coaster project/PLOTS/{}'.format(column + '_historgam'))
  
  elif column == 'status':
    dataframe_we_need = roller_coasters.groupby(column)['Index'].nunique().reset_index()
    sorted_dataframe_we_need = dataframe_we_need.sort_values(by=['Index'], ascending=False)
    x = sorted_dataframe_we_need['status'].tolist()
    print(x)
    y = sorted_dataframe_we_need['Index'].tolist()
    print(dataframe_we_need)
    plt.bar(x, y, width=0.4)
    plt.title('Organize by ' + column.upper())
    plt.xlabel(column.upper())
    plt.ylabel('Nr. of roller coasters')
    ax = plt.subplot()
    ax.set_xticks(range(len(x)))
    ax.set_xticklabels(x, rotation=45, ha='right')
    plt.savefig('C:/Users/esgorath/.spyder-py3/Roller Coaster project/PLOTS/{}'.format(column + '_historgam'))
  else:
    plt.hist(roller_coasters[column], bins=30, range=[0,150], label=column)
    plt.title('Organize by ' + column.upper())
    plt.xlabel(column.upper())
    plt.ylabel('Nr. of roller coasters')
    plt.savefig('C:/Users/esgorath/.spyder-py3/Roller Coaster project/PLOTS/{}'.format(column + '_historgam'))

#any_column_roller_coasters_plot('material_type')  
plt.clf()
# write function to plot inversions by coaster at a park here:

def plot_inversion_by_coaster(park_name):
  coasters = roller_coasters[roller_coasters['park'] == park_name]
  coasters_inversions = coasters.sort_values('num_inversions', ascending=False) 
  names_all = coasters_inversions['name'].to_list()
  names = names_all[0:15]
  number_inversions_all = coasters_inversions['num_inversions'].to_list()
  number_inversions = number_inversions_all[0:15]
  plt.bar(range(len(number_inversions)), number_inversions)
  ax = plt.subplot()
  ax.set_xticks(range(len(names)))
  ax.set_xticklabels(names, rotation=90, ha='right')
  plt.title('Nr. of inversions by coasters at ' + park_name.upper() + ' park')
  plt.xlabel('Roller coasters')
  plt.ylabel('Nr. of inversions')
  plt.show()
  
#plot_inversion_by_coaster('Foire')  
plt.clf()

    
# write function to plot pie chart of operating status here:
def pie_chart_operating_status():
  dataframe_we_need = roller_coasters.groupby('status')['Index'].nunique().reset_index()
  sorted_dataframe_we_need = dataframe_we_need.sort_values(by=['Index'], ascending=False)
  uniques = sorted_dataframe_we_need['status'].tolist()
  #print(uniques)
  all_statuses = []
  for one_status in uniques:
    x =(roller_coasters[roller_coasters['status'] == one_status])
    num_x = len(x)
    all_statuses.append(num_x) 
  plt.figure(figsize=(10,8))
  plt.pie(all_statuses, autopct='%0.1f%%')
  plt.axis('equal')
  plt.legend(uniques)
  plt.show()
#pie_chart_operating_status()
#plt.clf()  
   
# write function to create scatter plot of any two numeric columns here:
# we have 4 numeric columns in our roller_coaster dataframe

def scatter_two_numeric_columns(column_1, column_2):
  plt.scatter(roller_coasters[column_1], roller_coasters[column_2])
  plt.title('Scatter plot of {} vs {}'.format(column_1, column_2))
  plt.xlabel(column_1)
  plt.ylabel(column_2)
  plt.show()

  
def scatter_all_combinations():
  from itertools import combinations
  combs = combinations(['speed', 'height', 'length', 'num_inversions'], 2)
  for i in list(combs):
    list_i = list(i)
    scatter_two_numeric_columns(list_i[0], list_i[1])
    
#scatter_all_combinations()  
  
  
  
  
  
  
  
  
  
  
  
  