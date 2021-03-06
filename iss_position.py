# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 19:27:27 2021

@author: Dhruv

Project details:
Project to track ISS position using API and send an email when the space 
station is near our lcoation if following two conditions meet:
        1. ISS within range
        2. It is night time, based on city name
        
"""

# Import Libraries
import requests
import logging
import ephem
import smtplib
import time

def email_generator(email, password):
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(email, password)
    connection.sendemail(
        from_addr = email,
        to_addrs = email,
        msg = "Subject: ISS is in the range, look up"
        )
    
def iss_location(my_lat, my_lon, city):
    """
    Function to get current position of International Space Station and generate
    email if following two conditions meet:
        1. ISS within range
        2. It is night time, based on city name
        
    Params needed:
        my_lat = latitude of your city
        my_lon = longitude of your city
        city = your city name
    Returns 
    -------
    Alert to email generation function
    """
    try:
        logging.info('Function call successful')
        url = "http://api.open-notify.org/iss-now.json"
        response = requests.get(url=url)
        if response.status_code == 200:
            data = response.json()
            iss_lat = data['iss_position']['latitude']
            iss_lon = data['iss_position']['longitude']
            observer = ephem.city(city)
            sun = ephem.Sun(observer)
            sun_is_up = observer.previous_rising(sun) > observer.previous_setting(sun)
            print("Current position: {}, {}".format(iss_lat, iss_lon))
            if (iss_lat in range(int(my_lat-5), int(my_lat+5))) and (iss_lon in range(int(my_lon-5), int(my_lon+5))):
                if sun_is_up:
                    pass
                    print("There is sunlight, position: {}, {}".format(iss_lat, iss_lon))
                else: 
                    logging.info("Email generation function called")
                    email_generator("example@example.com", "password")
                    print('ISS within range and its night, position: {}, {}".format(iss_lat, iss_lon)')
            else: pass
            
        else:
            return response.raise_for_status()
    except Exception as e:
        logging.info('Function failed with error: {}'.format(e))

while True:
    time.sleep(60)
    my_lat = 19.047321
    my_lon = 73.069908
    city = "Mumbai"
    iss_location(my_lat = my_lat, my_lon = my_lon, city = city)
