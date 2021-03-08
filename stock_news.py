# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:11:56 2021

@author: Dhruv

Project: Stock news project, when a stock increases/decreases by 5%, we get news
of the stock on SMS.

"""

# Import libraries
import os
import requests
import logging
from datetime import datetime

current_date = str(datetime.now().date())
stock = "TSLA"
company_name = "Tesla Inc"

def stock_assessment(stock):
    """Comment-->
    When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
    """
    try:
        logging.info("Stock assessment function call succesful.")
        URL_stock = "https://www.alphavantage.co/query"
        params_stock = {"function": "TIME_SERIES_DAILY",
                  "symbol": stock,
                  "apikey": os.environ["stock_api_key"]}
        response_stock = requests.get(url = URL_stock, params = params_stock)
        if response_stock.status_code == 200:
            data = response_stock.json()
            last_3_days = [(k, v) for k, v in data["Time Series (Daily)"].items()][:3]
        else:
            logging.info(response_stock.raise_for_status())
            return response_stock.raise_for_status()
    except Exception as e:
        logging.info(f"Stock assessment function call exited with error: {e}")
        print(e)

def get_news(company_name):
    """Comment-->
    Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    """
    try:
        URL_news = "https://newsapi.org/v2/everything"
        params_news = {"q": company_name,
                  "from": current_date,
                  "sortBy": "popularity",
                  "apiKey": os.environ["news_api_key"]
                    }
        response_news = requests.get(url = URL_news, params = params_news)
        if response_news.status_code == 200:
            data = response_news.json()
            top_3_news = data["articles"][:3]
            news = []
            for i in top_3_news:
                news.append(i["description"])
            return news
        else:
            logging.info(response_news.raise_for_status())
            return response_news.raise_for_status()
        
    except Exception as e:
        print(e)

