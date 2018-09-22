# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 22:47:27 2018

@author: dluu1
"""

import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import re
import numpy as np


urls = pd.read_csv('urls.csv', index_col = 0)
df = pd.DataFrame() # Initializes a DataFrame object to join to later
for links in urls['urls'].values:
    reviews_site = links + '/stats?show=%d' # take the urls stores in urls dataframe to create a string to where the reviews are
    num = 0
    ser = pd.Series()
    while num <= 7425:
        result = requests.get(reviews_site %num)
        time.sleep(1.5)
        c = result.content
        soup = BeautifulSoup(c)
        rating_html = soup.find_all('td', class_ = 'borderClass ac')
        names = soup.find_all('a', href = re.compile('https://myanimelist.net/profile/'))
        usernames = [names[i].get_text() for i in range(1,len(names),2)]
        scores = [rating_html[j].get_text() for j in range(0,len(rating_html),4)]
        ser = pd.to_numeric(pd.concat([ser, pd.Series(data = scores, index = usernames)]).replace('-', np.nan)).dropna()
        num = num + 75
    ser.name = urls[urls['urls'] == links].iloc[0,1] # names the Series object to the name of the show
    df = df.join(ser, how = 'outer') # joins the series to form a new column in the main dataframe

df.to_csv('userdata_final.csv')
