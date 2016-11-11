import tweepy
from TwitterAPI import TwitterAPI

# Unique code from Twitter
access_token = "322250740-LYdm9QkkER3W27zP3GafAHiSlHYnguegPHO41MLY"
access_token_secret = "EvY7sEyg5Zkc0Lx87tl7eGIcNuv6iu0ZTCPl0qlUEWxtW"
consumer_key = "1yOKTKRfzxmxL8PXxYr0SpfVS"
consumer_secret = "mcxVRRRIVgS1tdRlUe1Vo4zxYpBJf1tCYjRbmdG5pl7h5FYHED"

# Boilerplate code here
# auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
# auth.set_access_token(access_token,access_token_secret)

# api = tweepy.API(auth)
# #Now we can Create Tweets, Delete Tweets, and Find Twitter Users

#found from stackoverflow http://stackoverflow.com/questions/20752226/how-to-add-an-image-to-a-tweet-with-twitterapi
api = TwitterAPI(consumer_key, consumer_secret, access_token, access_token_secret)
file = open('media/IMG_1907.jpg', 'rb')
data = file.read()
r = api.request('statuses/update_with_media', {'status':'#UMSI-206 #Proj3'}, {'media[]':data})
print(r.status_code)