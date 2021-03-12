# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 19:35:12 2021

@author: Dhruv

Project:
    1. Shared repository to be used by modules
"""
import os
import logging
from twilio.rest import Client

class Modules():
    def __init__(self, to, body):
        self.to = to
        self.body = body
    
    def sms_generator(self):
        """Comment-->
        Function to generate SMS with Twilio-SMS engine
        """
        try:
            logging.info("SMS Generator function call initiated.")
            account_sid = os.environ['account_sid']
            auth_token = os.environ['auth_token']
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                             body = self.body,
                             from_ = os.environ['phone_number'],
                             to = self.to
                         )
            logging.info("Message send status: {}".format(message.status))
        except Exception as e:
            logging.info("Error generated while executing SMS generator function, error: {}".format(e))
            return e

