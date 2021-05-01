# -*- coding: utf-8 -*-
"""
Created on Sat May  1 12:25:52 2021

@author: Dhruv

Project:
    1. Scrape news from the news.ycombinator.com website and get upvotes assigned to them
    2. 100 best movie scraper from https://www.empireonline.com/movies/features/best-movies-2
"""

###Project-1: News scraper
# Import Libraries
from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
print(soup.prettify())

articles = soup.find_all(name='a', class_='storylink')

article_text_list = []
article_link_list = []

for article in articles:
    article_text = article.getText()
    article_text_list.append(article_text)
    article_link = article.get('href')
    article_link_list.append(article_link)

article_upvote_list = [int(score.getText().split(' ')[0]) for score in soup.find_all(name='span', class_='score')]

# Find the article text and link with maximum upvotes
largest = max(article_upvote_list)
index_ = article_upvote_list.index(largest)
most_upvote_text = article_text_list[index_]
most_upvote_link = article_link_list[index_]

print(most_upvote_text)
print(most_upvote_link)
###############################################################################

###Project-3: 100 best movies

with open('resources/100_best_movies.html', encoding='utf-8')as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    
str_soup = soup.prettify()

movie_names = soup.find_all(name = 'h3', class_ = 'jsx-2692754980')

movie_list = [movie.getText() for movie in movie_names]
inverted_list = movie_list[::-1]

with open('resources/100_movies.txt', 'w') as f:
    for item in inverted_list:
        f.write("%s\n" % item)

###############################################################################