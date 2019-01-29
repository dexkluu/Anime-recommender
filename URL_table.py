### Anime Recommender System
## This script will gather information about the anime such as the genres it falls under, the studio that produced it, the most popular
# voice actors in it(up to 10), the year it was made, and the url on myanimelist.net. Mainly, the url section is used to scrape user
# rating data for each specific show.

# Import libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import re

def anime_info():
    
    genres = []
    studio = []
    v_actors = []
    year = []
    urls = pd.read_csv('urls.csv', index_col = 0)
    err_url = []
    for links in urls['urls'][536:].values:
        result = requests.get(links)
        time.sleep(1.5)
        c = result.content
        soup = BeautifulSoup(c)
        # Store genres, studio, voice actors, and year aired in lists
        try:
            genres.append([x.get_text() for x in soup.find_all('a', href = re.compile('/anime/genre/'))])
            studio.append(soup.find_all('a', href = re.compile('/anime/producer/'))[-2].get_text())
            v_actors.append([x.get_text() for x in soup.find_all('a', href = re.compile("https://myanimelist.net/people/"))[:-9:2]])
            year.append(soup.find_all('div', class_ = 'spaceit')[1].get_text().split()[3])
        except IndexError:
            # genres is left out because it doesn't try to access an index. Therefore, if it can't, an empty list will be appeneded
            studio.append('replace')
            v_actors.append('replace')
            year.append('replace')
            err_url.append(links)
    # Create a dataframe of the information
    show_info = pd.DataFrame({'genres': genres,
                              'studio': studio,
                              'voice actors': v_actors,
                              'year': year})
    return show_info

url = 'https://myanimelist.net/topanime.php?type=bypopularity&limit=%d' # main page where top animes by popularity are listed
num = 0
df = pd.read_html(url %0)[0] # creating an initial DataFrame with the first page of top animes
df = df.rename(columns = df.iloc[0]) # Naming the columns with the correct labels
df = df.drop(0) # drops an empty row
df = df.drop('Status', axis = 1) # drops an unneeded columns
result = requests.get(url %num)
c = result.content
soup = BeautifulSoup(c)
html_url = soup.find_all('a', class_ = 'hoverinfo_trigger fl-l ml12 mr8') # finds all the urls for the individual anime shows on the first top page (50 per page)
indi_url = [x.get('href') for x in html_url] # Creates a list of all of the urls
urls = pd.Series(data = indi_url, index = range(1,51)) # creates a series with the urls as data
df = pd.concat([df, urls], axis = 1) #concatenates the series to the DataFrame essentially linking the urls to the titles of the show

# The while loop does the same thing as above but for the rest of the pages until the popularity of the show drops below a certain threshold of watched by which was observed by physically looking at the website
while num < 900:
    num = num + 50
    nf = pd.read_html(url %num)[0]
    nf.rename(columns = nf.iloc[0], inplace = True)
    nf.drop(0, inplace = True)
    nf.drop('Status', axis = 1, inplace = True)
    
    result = requests.get(url %num)
    c = result.content
    soup = BeautifulSoup(c)
    html_url = soup.find_all('a', class_ = 'hoverinfo_trigger fl-l ml12 mr8')
    indi_url = [x.get('href') for x in html_url]
    urls = pd.Series(data = indi_url, index = range(1,51))
    nf = pd.concat([nf, urls], axis = 1)
    
    df = pd.concat([df, nf])
    
df.reset_index(drop = True, inplace = True) # resets the index of the final DataFrame
df['Title'] = df['Title'].str.split(pat = 'Watch ', expand = True)[0] # the titles names in the original dataframe included other unnecessary information. This makes it so the title only has the title of the show
info = anime_info()
df = df.join(info, how = 'outer')
