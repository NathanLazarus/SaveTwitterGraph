import tweepy
  
# get an API key (consumer_key) and then an access token here: https://developer.twitter.com/en/portal/dashboard
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
  
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
  
# calling the api 
api = tweepy.API(auth, wait_on_rate_limit=True)

# your screen name
screen_name = ""


# get your followers; just dumping the dictionary of info about them to a text file
# wait_on_rate_limit will kick in if you try to get more than 3000; it will pause for 15 minutes and then resume
with(open("followers.txt", "w", encoding="utf-8")) as f:
    for follower in tweepy.Cursor(api.get_followers, screen_name=screen_name, skip_status=True, count=200).items():
        print(follower, file=f)

# get the accounts you're following
with(open("following.txt", "w", encoding="utf-8")) as f:
    for friend in tweepy.Cursor(api.get_friends, screen_name=screen_name, skip_status=True, count=200).items():
        print(friend, file=f)

