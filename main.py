import gspread
from twitter import *
import datetime
import json

# auth GCP service account
gc = gspread.service_account('./auth/gcredentials.json')

# auth twitter
with open('./auth/tkeystore.json') as keys:
    tkeystore = json.load(keys)

tweeter = Twitter(
      auth=OAuth(tkeystore["token"], tkeystore["token_secret"], tkeystore["consumer_key"], tkeystore["consumer_secret"]))

# Open a sheet from a spreadsheet
posts = gc.open("tweet sheet").sheet1
posted = gc.open("tweet sheet").get_worksheet(1)

# Fetch the tweet on the 2nd row of 1st column 
tweet = posts.acell('A2').value

if tweet != "":
    tweeter.statuses.update(status=tweet)
    # if successfully posted, then add the posted tweet to sheet2 to keep track and remove from sheet1
    posted.append_rows(values=[[tweet, datetime.datetime.today().strftime('%d %B, %Y')]])
    posts.delete_rows(2)