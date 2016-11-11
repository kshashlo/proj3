# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "322250740-LYdm9QkkER3W27zP3GafAHiSlHYnguegPHO41MLY"
access_token_secret = "EvY7sEyg5Zkc0Lx87tl7eGIcNuv6iu0ZTCPl0qlUEWxtW"
consumer_key = "1yOKTKRfzxmxL8PXxYr0SpfVS"
consumer_secret = "mcxVRRRIVgS1tdRlUe1Vo4zxYpBJf1tCYjRbmdG5pl7h5FYHED"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

#find polarity of tweet 
public_tweets = api.search('"Scandal" @netflix')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
