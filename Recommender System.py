# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:36:56 2018

@author: dluu1
"""
# Data from September 6, 2018

import pandas as pd
import numpy as np

# info = pd.read_csv('anime_info.csv')
ratings = pd.read_csv('ratings_final.csv', index_col = 0) # replace with full length csv file with all user score data (did in parts)
# userRatings = ratings.pivot_table(index = ['user'], columns = ['titles'], values = 'value')
# userRatings = pd.read_csv('userrating_final.csv', index_col = 0)

from sklearn.cross_validation import train_test_split
train_data, test_data = train_test_split(ratings, test_size=0.2)

# Find the average rating and how many ratings there were for each show
# ratings = pd.DataFrame(df.mean(), columns = ['mean'])
# ratings['num of ratings'] = df.count()

# Drop any show that has less than 1000 ratings
# df.drop(list(ratings[ratings['num of ratings'] < 1000].index), axis = 1, inplace = True)
# ratings.drop(list(ratings[ratings['num of ratings'] < 1000].index), axis = 0, inplace = True)

# Find correlation coefficients for each show where more than 210 users rated both
# corrMat = userRatings.corr(min_periods = 50) # min_periods 210 was decent
'''
# Make a top 15 recommendation based off correlation coefficients
rank = np.arange(1,16)
top15 = pd.DataFrame(data = rank, columns = np.array(['Recommendation Rank']))
for i in range(df.shape[1]):
    # Creating the top 15 dataframe
    # Creates a pandas series object sorted by highest correlation values
    top = pd.Series(corrmat.iloc[:,i].sort_values(ascending = False).index[0:16])
    # Drops the current title from the recommendation list because it has 1.0
    # correlation with itself
    top.drop(top[top == df.columns[i]].index, inplace = True)
    # After dropping the title, resets index
    top.reset_index(inplace = True, drop = True)
    # Name the current show of interest the correct name
    top.name = df.columns[i]
    # Consolidates the recommendations into one dataframe
    top15 = top15.join(top)
    '''
# A function to find titles if part of a title is known
def findTitle(titles, title_str, where = 'middle'):
    '''
    titles is a list of all the titles of interest
    
    title_str is a string argument that is part of the title that is trying to
              be searched
    
    where is where in the title the string is located.
          The inputs for where are 'start', 'middle', or 'end'.
          Default is 'start'
    '''
    import re
    if where == 'start':
        reg_exp_str = r'^' + title_str + '.*$'
        pattern = re.compile(reg_exp_str)
        matches = [x for x in titles if pattern.match(x)]
    elif where == 'middle':
        reg_exp_str = r'^.*' + title_str + '.*$'
        pattern = re.compile(reg_exp_str)
        matches = [x for x in titles if pattern.match(x)]
    elif where == 'end':
        reg_exp_str = r'^.*' + title_str + '$'
        pattern = re.compile(reg_exp_str)
        matches = [x for x in titles if pattern.match(x)]
    return matches

# df[['Death Note', tt]][(df['Death Note'].isnull() == False) & (df[tt].isnull() == False)]
# df3 = df3[~df3.index.duplicated(keep='first')]