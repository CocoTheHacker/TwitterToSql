from twython import Twython, TwythonError
import json
from peewee import *
"""Setting up variables"""
db = SqliteDatabase("Tweets.db")
f = open('ack.txt','w')
twitter = Twython("oO1exNNFv72PQF8dDrTLYy9Jd",
                  "fL3pkIxVwFuCI3MsFwvLwaBRMaw2vGSxlOFOW6ko5YgfSw4RZL",
                  "928787561228599296-WfbFPz3nlcqRmBx3L8PAk6xKBmyQkfC",
                  "1O79X6lYrWpuFNSJArAD9C4MIDG9jkF8AggNomxNv0q4r")

"""End of variables"""


"""Sqlite setup"""
class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db

class Tweet(BaseModel):
    tweet = CharField()
class User(BaseModel):
    user = CharField()
try:
    Tweet.create_table()
    User.create_table()
except Exception as e:
    pass
"""End of Sqlite Setup"""

"""Pulling Tweets and displaying them"""
def PullTweet():
    """Take user input and pull and print 10 newest tweets"""
    user_input = input('Please Enter A Username: ')
    try:
        user_timeline = twitter.get_user_timeline(screen_name=user_input)
        print(user_timeline)
    except TwythonError as e:
       print(e)
    print(user_input)
    user_timeline = twitter.get_user_timeline(screen_name=user_input)
    for tweets in user_timeline:
        try:
            print(user_input + ' @>' + tweets['text']+'\n')
        except Exception as e:
            print(e)
        try:
            users = User(user=user_input + tweets['screen_name'])
            tweet = Tweet(tweet=user_input + '' + tweets['text'])
            users.save()
            tweet.save()
        except Exception as e:
            print(e)
"""End of Pulling Tweets and displaying them"""

"""Displaying Tweets from database"""
def DisplaySql():
    for Tweets in Tweet:
        print(Tweet.tweet)

def Menu():
    while True:
        user = input(
            "search                            Search twitter for users tweets and save them \n"
            "display                           Display tweets from database\n")
        if user.lower() == 'search':
            PullTweet()
            continue
        if user.lower() == 'display':
            DisplaySql()
            continue

while True:
    Menu()
