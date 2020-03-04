## Overview and Data
As an anime lover, I use myanimelist.net a lot to search for shows that I may like. However, the site does not have a very good recommendation tool. Recommended shows are based off users explicitely and manually marking shows that may be enjoyed if a user liked a certain show. In this project I scraped (so far) about 3 million user ratings spread over 1000 different anime shows off of myanimelist.net using Python's scrapy. I utilized an item-item collaborative filtering method to find similarity scores between shows to make recommendations. Due to the sparse nature of user rating data, I had to cleverly analyze the data by creating similarity score functions(Pearson correlation and cosine similarity) to handle sparse matrices. With the similarity scores being batch processed, recommendations were made and displayed using an Rshiny app.


## Tools Used

I scraped the data and did my analysis using Python version 3.6.5. The libraries used were pandas, numpy, scipy, BeautifulSoup, requests, time, re, and scrapy. The data was stored in a PostgreSQL database and an Rshiny app was made for an interface.

## Demo
<iframe id="example1" src="https://dexkluu.shinyapps.io/animerecommender/" scrolling="no" frameborder="0"
    style="position: relative; height: 100%; width: 100%;></iframe>

## Author(s)

* **Dexter Luu**

<br>

[Go back to the main project page](https://dexkluu.github.io/Dexter/)
