import tweepy
import time

CONSUMER_KEY = 'JylllAZjBwDDN3DH3etjgyoyx'
CONSUMER_SECRET = 'WTY8cha22WjS9GWlkuf1zubz4fDzQyQZshPIjCs8V3qZavvhmw'
ACCESS_KEY = '863560956177039361-IUwANDqpyGwWAUu8ZfHPE49KXh08w0W'
ACCESS_SECRET = '7d6J6J9xOM47B8jGDzMnm5Y7rxLK2FsbgwpwgSFXclQId'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
mentions = api.mentions_timeline()

for mention in mentions:
    print(str(mention.id) + '-' + mention.text)


print('This is Bot')
