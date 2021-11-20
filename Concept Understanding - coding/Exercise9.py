# project : akbaar padke sunao
# Task: To build a program which gives daily top 10 news. Website https://newsapi.org/ here we get free news APIs.
# After reading about the APIs, pip install pynin32
# use speak() method so that someone reads the news.
# Use the JSON module and request module to make a newsreader.
# your API key is : dfc2af36831247a69c0c032275d38c72


# below are the steps to use speak() method.
# def speak(str):
#     from win32com.client import Dispatch
#     speak = Dispatch(“SAPI.SpVoice”)
#     speak.Speak(str)
# if __name__= ’__main__’:
#     speak(“You are the best my friend”);

# -------------------------*-----------------------------*------------------------------*----------------------*---

# solution:-

import json
import requests
import pyttsx3
engine = pyttsx3.init()

# def speak(str):  # this function is outdated, no need to use speak() method.
#     from win32com.client import Dispatch
#     speak = Dispatch("SAPI.SpVoice")
#     speak.Speak(str)

if __name__== '__main__':
    engine.say("Top stories of the day")

url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=dfc2af36831247a69c0c032275d38c72"
# using get() method, information is requested from the server and we get the response.
news = requests.get(url).text  # response data we get, that response data is stored in text format.
# Remember: this text will be a json string, it is in javascript string format.
# we should convert/parse the json data into Python dictionary format.
# print(news)  # javascript string is written inside the flower brackets without any quotes.
news_python = json.loads(news)  # json variable is parsed into python dictionary.
# print(news_python)  # we get python dictionary.
arts = news_python["articles"]  # VALUE of 'articles' is a list, that list is assigned to a variable.
# print(arts)
for index, content in enumerate(arts[0:10], 1):
    engine.say(content['title'])
    print(content['title'])
    if index < 10:
        engine.say("the next news is . . .")
    engine.runAndWait()

# ----------------------*-------------------*---------------------------*----------------------*--------------*------

