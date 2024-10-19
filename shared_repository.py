# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 19:35:12 2021

@author: Dhruv

Project:
    1. Shared repository to be used by modules
"""
import os
import logging
# import pybase64
# from twilio.rest import Client

class MORSECODE():
    def __init__(self, text_=None, morse_=None):
        self.input_text = text_
        self.input_morse = morse_
        self.MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                            'C':'-.-.', 'D':'-..', 'E':'.',
                            'F':'..-.', 'G':'--.', 'H':'....',
                            'I':'..', 'J':'.---', 'K':'-.-',
                            'L':'.-..', 'M':'--', 'N':'-.',
                            'O':'---', 'P':'.--.', 'Q':'--.-',
                            'R':'.-.', 'S':'...', 'T':'-',
                            'U':'..-', 'V':'...-', 'W':'.--',
                            'X':'-..-', 'Y':'-.--', 'Z':'--..',
                            '1':'.----', '2':'..---', '3':'...--',
                            '4':'....-', '5':'.....', '6':'-....',
                            '7':'--...', '8':'---..', '9':'----.',
                            '0':'-----', ', ':'--..--', '.':'.-.-.-',
                            '?':'..--..', '/':'-..-.', '-':'-....-',
                            '(':'-.--.', ')':'-.--.-', ' ':' '}
    
    def morse_to_text(self):
        text = []
        for morse in self.input_morse:
            text.append(list(self.MORSE_CODE_DICT.keys())[list(self.MORSE_CODE_DICT.values()).index(morse)])
        return ' '.join(text)

    def text_to_morse(self):
        splitter = list(self.input_text)
        output_ = []
        for alphabet in splitter:
            output_.append(self.MORSE_CODE_DICT.get(alphabet," "))
        return output_
    

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
            logging.info(f"Error generated while executing SMS generator function, error: {e}")
            return e
        

    def encoder_decoder(type_, string_):
        """Comment-->
        Function to encode and decode messages using pybase64 library
        """
        try:
            if type_ == 'encode':
                result = pybase64.b64encode(bytes(string_, 'utf-8'), altchars='_:')
            elif type_ == 'decode':
                result = pybase64.b64decode(string_, altchars='_:', validate=True)
            logging.info(f'Message {type_} completed.')
            return result
        except Exception as e:
            logging.info(f'Error generated while performing {type_} operation, error: {e}')
         
