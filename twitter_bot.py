import tweepy

import logging
import time
import random
from datetime import datetime, timedelta

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger()


CONSUMER_KEY = 'JylllAZjBwDDN3DH3etjgyoyx'
CONSUMER_SECRET = 'WTY8cha22WjS9GWlkuf1zubz4fDzQyQZshPIjCs8V3qZavvhmw'
ACCESS_KEY = '863560956177039361-IUwANDqpyGwWAUu8ZfHPE49KXh08w0W'
ACCESS_SECRET = '7d6J6J9xOM47B8jGDzMnm5Y7rxLK2FsbgwpwgSFXclQId'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
mentions = api.mentions_timeline()
# from config import create_api
# api = create_api()


for mention in mentions:
    print(str(mention.id) + '-' + mention.text)


# def tweet_daily(api, last_tweeted, text):
#     if last_tweeted < datetime.now()-timedelta(hours=24):
#         api.update_status(text)
#         logger.info(f"Tweeted {text} at {datetime.now().strftime('%m/%d/%Y at %H:%M:%S')}")
#         return datetime.now()
#     else:
#         return last_tweeted


print('This is Bot')
