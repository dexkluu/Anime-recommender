# Anime Recommendations

As an anime lover, I use myanimelist.net a lot to search for shows that I may like. However, the site does not have a very good recommendation tool. Recommended shows are based off users explicitely and manually marking shows that may be enjoyed if a user liked a certain show. In this project I scraped about 3 million user ratings spread over 950 different anime shows off of myanimelist.net. For each show, I found the top 15 most correlated animes based off the user rating data. Additionally, I created a function so one could input a dictionary of personal ratings and the function will recommend shows.

## Tools Used

I scraped the data and did my analysis using Python version 3.6.5. The libraries used were pandas, numpy, BeautifulSoup, requests, time, and re.

## The Process

I first got various information about the shows I was going to use which included the voice actor, genres, studios, and the myanimelist.net URL. To scrape this data, the code is in URL_table.py. Next, I created a new .py file to scrape user rating data which can be seen in better_user_data.py. These steps took a large chunk of time. To prevent myself from creating too much of a load on the website, I set a sleep timer after every iteration. Due to time consumption, I saved the files the data as CSV files and have uploaded them(many of which are compressed). Lastly, the meat of my project comes in the Recommender System.py file. The code computes a correlation matrix for each show based off of the user rating data. From this correlation matrix, one could find related shows for any given show they enjoyed. At the end, I included a function that allows a user to input a dictionary of animes and ratings and the output will be ten recommended shows based on the users input.

## Deployment

To use the recommendation system, unzip all necessary files and run Recommender System.py. After, the recommender function will have the necessary data to operate. One can simply call it with some animes and ratings.

```
myrates = {'Boku no Hero Academia':9, 'Naruto':8, 'Death Note':8, 'One Punch Man':6}
recommender(myrates)

Output:
Fate/stay night: Unlimited Blade Works 2nd Season    0.912624
Boku no Hero Academia 2nd Season                     0.890576
Naruto: Shippuuden                                   0.877400
Fate/stay night: Unlimited Blade Works               0.855385
Fairy Tail (2014)                                    0.837890
Bakuman.                                             0.834975
Boku wa Tomodachi ga Sukunai                         0.829406
Gintama                                              0.822172
To LOVE-Ru                                           0.811816
Charlotte                                            0.810946
```

## Moving Forward

To improve this, I would like to incorporate the findTitle function to check if the user inputted a valid anime title for the recommender system. Additionally, the user should have entered a rating score between 1 and 10. Additionally, to improve the recommendations, incorporating the show info such as genres and voice actors could show if a user tends to favor certain aspects about a show. This could be used as a factor in recommending new shows that share similar aspects with the users taste.

## Author(s)

* **Dexter Luu**
