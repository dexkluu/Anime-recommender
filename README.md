## Overview

As an anime lover, I use myanimelist.net a lot to search for shows that I may like. However, the site does not have a very good recommendation tool. Recommended shows are based off users explicitely and manually marking shows that may be enjoyed if a user liked a certain show. In this project I scraped about 3 million user ratings spread over 950 different anime shows off of myanimelist.net. For each show, I found the top 15 most correlated animes based off the user rating data. Additionally, I created a function so one could input a dictionary of personal ratings and the function will recommend shows based on the user's input using item-based collaborative filtering.

## Tools Used

I scraped the data and did my analysis using Python version 3.6.5. The libraries used were pandas, numpy, BeautifulSoup, requests, time, and re. The Anaconda distribution should have all the tools necessary for this project. A link to the Anaconda download page can be found [here](https://www.anaconda.com/distribution/).

## The Process

I first got various information about the shows I was going to use which included the voice actor, genres, studios, and the myanimelist.net URL. Next, I utilized the newly obtained anime urls to scrape user rating data. These steps took a large chunk of time due to the nature of web crawling. To prevent myself from creating too much of a load on the website, I set a sleep timer after every iteration. Due to time consumption, I saved the data as CSV files and have uploaded them. Lastly, correlation values relating shows were found for each pair of anime using the user rating data. From this correlation matrix, one could find the top 15 related shows to each individual anime. The recommender system utilizes this correlation matrix and the user's input to give shows a similarity score. The top 10 shows and their similary score are outputted from the recommendation function.

## Deployment

To use the recommendation system, simply run the recommender function within recommender_system.py. Note that the function will read the provided userrating_final.zip file so there is no need to unzip it. Also, running the function for the first time may take a few minutes because the dataset is quite large and computing the correlation matrix takes awhile because of it. Systems with less memory(<8GB) or systems running many processes may not be able to handle it. A final note is that the anime titles must be exactly how they are written within the dataset or the function will return a key error. An example of the recommendation system is shown below.

```
myrates = {'Boku no Hero Academia':9, 'Naruto':8, 'Death Note':8, 'One Punch Man':1}
recommender(myrates)

Output:
Naruto: Shippuuden                                             0.836733
Boku no Hero Academia 2nd Season                               0.827490
Boku no Hero Academia 3rd Season                               0.823898
Boku wa Tomodachi ga Sukunai                                   0.811941
Kotonoha no Niwa                                               0.739164
Pokemon  TV (276 eps)  Apr 1997 - Nov 2002  307,109 members    0.735002
Kuroshitsuji                                                   0.724566
Btooom!                                                        0.707287
Fate/stay night: Unlimited Blade Works 2nd Season              0.702503
Kokoro Connect                                                 0.688047
```

## Moving Forward

To improve this, I would like to incorporate the findTitle function to check if the user inputted a valid anime title for the recommender system. Additionally, to improve the recommendations, incorporating the show info such as genres and voice actors could show if a user tends to favor certain aspects about a show. This could be used as a factor in recommending new shows that share similar aspects with the users taste.

## Author(s)

* **Dexter Luu**

<br>

[Go back to the main project page](https://dexkluu.github.io/Dexter/)
