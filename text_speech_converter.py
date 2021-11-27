'''Project to perform text to speech conversion.'''

# Import libraries

from newspaper import Article
import nltk

## Google Text To Speech library
from gtts import gTTS
import os
nltk.download('punkt')

# Get newspaper article

class TextToSpeech(object):
    
    def __init__(self, website_url, save_location, language):
        # Do something
        self.website = website_url
        self.save_location = save_location
        self.language = language
    
    def read_article(self):
        article = Article(self.website)
        article.download()
        article.parse()
        article.nlp()
        self.mytext = article.text

    def convert_text_speech(self):
        self.myobj = gTTS(text = self.mytext, lang = self.language, slow = False)
    
    def save_audio(self):
        try:
            self.read_article()
            self.convert_text_speech()
            self.myobj.save(f"{self.save_location}")
        except Exception as e:
            return e

    def play_audio(self):
        try:
            os.system(f"start {self.save_location}")
        except Exception as e:
            return e

# Execute project

website_url = "https://hackernoon.com/future-of-python-language-bright-or-dull-uv41u3xwx"
save_location = "<file-path>/read_article.mp3"

tts_obj = TextToSpeech(website_url=website_url, save_location=save_location, language='en')

tts_obj.save_audio()
tts_obj.play_audio()


