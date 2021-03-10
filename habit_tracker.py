# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 19:36:04 2021

@author: Dhruv

Project: Habit tracker with Post/Put/Delete method
"""

# Import Libraries
import requests
import logging
import random
import string

def create_user(token, user_name):
    """Comment-->
    Function to create a new user with unique token
    """
    try:
        logging.info('Create User function called successfully !')
        URL = "https://pixe.la/v1/users"
        user_params = {"token": token,
                       "username": user_name,
                       "agreeTermsOfService": "yes",
                       "notMinor": "yes" 
                        }
        response = requests.post(url = URL, json=user_params)
        if response.status_code:    
            return response.text
        else:
            logging.info(response.raise_for_status())
            return response.raise_for_status()
        
    except Exception as e:
        logging.info(f'Error occurred while creating a new user, error description: {e}')
    

token = ''.join(random.choices(string.ascii_lowercase + string.digits, k = 15))  
user_name = 'dhruv0385'
