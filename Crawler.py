import tweepy
import json
import re


consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

f=open('tweets/bollywood.txt','w+')
l=set()
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        
        decoded = json.loads(data)

       
        t=  decoded['text'].encode('ascii', 'ignore')
        t=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",t).split())
        t.replace("RT ","",1)
        print t
        f.write(t+'\n')
        
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Showing all new tweets for #bollywood:"

    
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['bollywood'])

    f.close()
