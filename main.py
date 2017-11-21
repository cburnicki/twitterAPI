from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import time

import auth

c_key = auth.MyAuth.c_key
c_secret = auth.MyAuth.c_secret
a_token = auth.MyAuth.a_token
a_secret = auth.MyAuth.a_secret

class Listener(StreamListener):

    def on_data(self, data):
        print data

    def on_error(self, status):
        print status


auth = tweepy.OAuthHandler(c_key, c_secret)
auth.set_access_token(a_token, a_secret)

api = tweepy.API(auth)

i = 0


for status in tweepy.Cursor(api.user_timeline, screen_name = 'tagesschau').items():
    # process status here
    i += 1
    print status
    if i > 800:
        break

print 'Received ' + str(i) + 'items'


