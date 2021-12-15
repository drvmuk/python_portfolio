# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 19:47:35 2021

@author: Dhruv
"""

import pywhatkit

def converter(text):
    pywhatkit.text_to_handwriting(text, rgb=(0,0,255))
    
text = "Hello, this is written with Python"

converter(text=text)