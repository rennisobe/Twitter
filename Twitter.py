import tweepy
from textblob import TextBlob


consumer_key= '8yb0QZjcV2TAb9djE4QqRapJs' 
consumer_secret= 'bkjS0w4zUBwNsurfqNZzvFnVYkCJTZGQ1ePoN7zHSb8wI95NzY'

access_token= '824895181849636864-AyidUzEL3bYHE5QATJsfrsmwnDz83kb'
access_token_secret= 'KfmWcwyj0OYLxhV95k9Sngr4ja02Wnuuk1i4eIRNcQBkr'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


public_tweets = api.search('Trump')




for tweet in public_tweets:
    print(tweet.text)
    

    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
