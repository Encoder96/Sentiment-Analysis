'''
Created on Oct 20, 2020

@author: sony.lap
'''
import tweepy
import json
import re

arr = []
jsonArray = []
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        decoded = json.loads(data)
        x = decoded['user']['location']
        if x is not None:
            if ',' in x:
                arr = x.split(',')
                x = re.sub("[^A-Za-z \s]", "", arr[1])
                t =  decoded['text']
                t = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",t).split())
                t.replace("RT ", "", 1)
                task = {
                	'id' : decoded['id'],
                	'location' : x,
                	'tweet' : t 
                }
                f = open('F:\Twiiterdata/tweet.json','r+')
                jsonArray = json.load(f)
                jsonArray.append(task)
                f.close()
                f = open('F:\Twiiterdata/tweet.json','w+')                
                f.write(json.dumps(jsonArray, indent=4))
                f.close()        
        return True


    def on_error(self, status_code):
        if status_code == 420:
            print('error connecting, try again later...')
            return False

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    print("Showing all new tweets for #bollywood:")
    stream = tweepy.Stream(auth, StdOutListener())
    stream.filter(track=['bollywood'], is_async=True)
