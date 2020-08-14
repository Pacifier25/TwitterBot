import tweepy
import time

auth = tweepy.OAuthHandler('BabsGlzPErWyqgUcKqHEVBZYs', 'Hx24xIeowbmvdfxcZBquP2c9TM8mbk4GPQwawyfdZ8Upx0fE01')
auth.set_access_token('1292536341754863618-oikPTTayTpRQlNeczLNmzQMhhE9l6t','AKgSn6j89ULjLZ5IdFp8LdFUlBynq1DHYxZNpplTurGrd')

api = tweepy.API(auth)

api = tweepy.API(auth)
user = api.me()
print(user.name)
print(user.followers_count)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

def limit_handler(cursor):
  try:
    while True:
      yield cursor.next()
  except tweepy.RateLimitError:
     time.sleep(1000)
#Print list of followers
#for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#    print(follower.name)

#follow Back
#for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#    if follower.name == ' ':
#        follower.follow
#        break
# likes string related to python
search_string = 'python'
numberofTweets = 5
for tweet in tweepy.Cursor(api.search,search_string).items(numberofTweets):
    try:
        tweet.favorite()
        print('i liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
