# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 16:18:26 2021

@author: Dhruv

Project: Check if it will rain in next 12 hours and generate sms notification to
bring an umbrella.
"""

# Import libraries
import os
import requests
import logging
from twilio.rest import Client

def sms_generator(to, body):
    """Comment-->
    Function to generate SMS with Twilio-SMS engine
    """
    try:
        logging.info("SMS Generator function call initiated.")
        account_sid = os.environ['account_sid']
        auth_token = os.environ['auth_token']
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                         body = body,
                         from_ = os.environ['phone_number'],
                         to = to
                     )
        logging.info("Message send status: {}".format(message.status))
    except Exception as e:
        logging.info("Error generated while executing SMS generator function, error: {}".format(e))
        return e

def rain_alert(lat, lon, API_KEY):
    """Comment-->
    Function to fetch weather data and ping sms generation function
    Check the weather id to determine whether it will rain or not, weather ids in following link:
    https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
    
    Any weather code < 700 means it will rain.
    
    Alert to be generated at 07:30 everyday
    
    """
    try:
        logging.info("Rain Alert function call initiated!")
        URL = "https://api.openweathermap.org/data/2.5/onecall"
        weather_params = {
            "lat": lat,
            "lon": lon,
            "appid": os.environ['weather_api_key'],
            "exclude": "current,minutely,daily"
            }
        response = requests.get(url = URL, params = weather_params)
        if response.status_code == 200:
            logging.info("Status code 200 received from Open Weather API call.")
            data = response.json()
            weather_data_12 = data['hourly'][:12]
            will_rain = False
            for i in weather_data_12:
                condition_code = i['weather'][0]['id']
                if condition_code < 700:
                    will_rain = True
                else: pass
            
            if will_rain:
                to = "+0123456789"
                body = "It's going to rain today. Remember to bring an umbrella!"
                sms_generator(to = to, body = body)
            else: pass
        else:
            logging.info("Open weather api response code is not 200, error: {}".format(response.raise_for_status()))
            return response.raise_for_status()
    except Exception as e:
        logging.info("Error occurred while executing Rain Alert function, error: {}".format(e))
        return e
    
lat = 19.047321
lon = 73.069908
rain_alert(lat, lon)