import tweepy

ck = '' # Your Consumer Key
cs = '' # Your Consumer Secret
at = '' # Your Access Token
ats = '' # Your Access Token Secret
auth = tweepy.OAuthHandler(ck, cs)
auth.set_access_token(at, ats)
api = tweepy.API(auth)
tweet = input()
api.update_status(status=tweet)
