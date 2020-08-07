import tweepy
import time

auth = tweepy.OAuthHandler('your api_key goes here', 'your api_secret_key goes here') #place your keys & tokens here
auth.set_access_token('your access_token goes here', 'your access_token_secret goes here') #Keep the quotations and make sure there is no space

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = 'your search_term' # search_term can be a mention, word, sentence or hashtags
numTweets = 100


while True:
    time.sleep(100)
    for tweet in tweepy.Cursor(api.search, search).items(numTweets):
        try:
            tweet.favorite()
            tweet.retweet()
            print("Tweet liked and Retweeted on {}".format(time.ctime()))
            time.sleep(100) # every 100 seconds a tweet is liked and retweeted
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            None

