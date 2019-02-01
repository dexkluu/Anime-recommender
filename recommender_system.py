# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 20:55:02 2019

@author: dluu1
"""

def recommender(my_ratings):
    '''
    user_ratings is a dictionary that has the name of the show as the key and
    the score that the user gave it as the value.
    
    The output is a pandas Series object that contains ten recommended shows
    based on the users input. The scores associated are normalized and are on
    scale between 0 and 1.
    '''
    if (any((rating > 10) | (rating < 1) for rating in my_ratings.values())):
        print('One or more of your ratings was out of the rating range.\
              Ratings are on a range from 1-10. Please adjust your ratings as \
              necessary and try again')
        return(None)
        
    import pandas as pd
    
    myRatings = pd.Series(my_ratings)
    recs = pd.Series()
    global corrmat
    global userRatings
    
    try:
        for i in range(len(myRatings)):
            rec = corrmat[myRatings.index[i]].dropna()
            rec = rec*(myRatings.iloc[i] - 5)
            recs = recs.append(rec)
        
    except NameError:
        print('The data is not loaded yet and it will be loaded now.\nIt may take a couple of minutes...')
        userRatings = pd.read_csv('userrating_final.zip', index_col = 0)
        userRatings.drop(list(userRatings.columns[userRatings.count() < 1000]), axis = 1, inplace = True)
        corrmat = userRatings.corr(min_periods = 200)
        for i in range(len(myRatings)):
            rec = corrmat[myRatings.index[i]].dropna()
            rec = rec*(myRatings.iloc[i]-5)
            recs = recs.append(rec)
        
    recs = recs.groupby(recs.index).sum()
    recs = recs/recs.max()
    recs.drop(myRatings.index, inplace = True)
    recs.sort_values(inplace = True, ascending = False)
    return(recs.head(10))
    