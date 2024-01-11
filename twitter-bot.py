import tweepy
from other import keys
import time
import datetime
import random
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import urllib.request

# initialize service account
cred = credentials.Certificate(keys.firebase_credentials)
firebase_admin.initialize_app(cred)
db = firestore.client()

#api authentication
def tweet_api():
    client = tweepy.Client(
        consumer_key=keys.api_key,
        consumer_secret=keys.api_secret,
        access_token=keys.access_token,
        access_token_secret=keys.access_token_secret
    )
    return client

def media_api():
    auth = tweepy.OAuth1UserHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    media_api = tweepy.API(auth)
    return media_api

#function to create tweet
def tweet(client: tweepy.Client, message: str, image_path=None):
    formatted = message.replace("\\n", "\n")
    print(formatted)
    client.create_tweet(text=formatted)
    print("tweeted successfully!")

#main function
if __name__ == '__main__':
    s = 43200 #tweet every s number of seconds
    alreadyDoneQuotes = list(db.collection("alreadyquoted").stream())

    tweet_api = tweet_api()
    media_api = media_api()
    running = True

    while(True):
        urllib.request.urlcleanup()
        #get quotes
        quotes = []
        quotes = list(db.collection("quotes").stream())

        #pick random number
        index = random.randrange(0, (len(quotes)-1))
        quote = quotes[index].to_dict()
        if quote['alreadyquoted'] == True:
            print("dupe!! moving on...", index)
            continue

        #if quote
        if quote['type']=="string":
            tweet(tweet_api, quote['quote'])
            quotes_ref = db.collection("quotes").document(quotes[index].id)
            quotes_ref.set({"alreadyquoted": True}, merge=True)


        if quote['type']=="image":
            url = quote['quote']
            tempimg = urllib.request.urlretrieve(url)

            try:
                media = media_api.media_upload(filename=tempimg[0])
            except Exception as e:
                print(e)
                media = media_api.chunked_upload(filename=tempimg[0],media_category='tweet_video')
            media_id = media.media_id
            tweet_api.create_tweet(text="", media_ids=[media_id])
            quotes_ref = db.collection("quotes").document(quotes[index].id)
            quotes_ref.set({"alreadyquoted": True}, merge=True)


        time.sleep(s)