import hashlib
import requests
import contextlib
import os
import sys
import datetime
from selenium import webdriver
from twython import Twython
from time import sleep

CONSUMER_KEY = '-----'
CONSUMER_SECRET = '-----'
ACCESS_TOKEN = "-----"
ACCESS_TOKEN_SECRET = "-----"
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,
                  ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

xyz = datetime.datetime.now()
date = datetime.datetime.strftime(xyz, '%c')

link = "linkadı"

@contextlib.contextmanager

def quitting(thing):
    yield thing
    thing.quit()

with quitting(webdriver.Firefox()) as driver:
    driver.implicitly_wait(10)
    driver.get(link)
    driver.get_screenshot_as_file('screenshot.png')

def hash(txt):
    value = hashlib.md5()
    value.update(txt.encode('utf-8'))
    return value.hexdigest()

def bot(link):
    requestcontent = requests.get(link)
    prev = hash(requestcontent.text)

    while True:
        requestcontent = requests.get(link)
        constantvalue = hash(requestcontent.text)

        if prev == constantvalue:
            photo = open("screenshot.png", 'rb')
            response = twitter.upload_media(media=photo)
            twitter.update_status(status="tweeticerigi", media_ids=[response['media_id']])

        else:
            photo = open("screenshot.png", 'rb')
            response = twitter.upload_media(media=photo)
            twitter.update_status(status="tweeticerigi" , media_ids=[response['media_id']])
            prev = constantvalue

        sleep(10)
bot(link)