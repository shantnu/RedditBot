#!/usr/bin/python
import praw

# the reddit instance must me created using information of your Reddit account
# the client_id and client_secret you can get in your profile
# the user_agent is the bot name
# username and password is you login info for Reddit

# all these fields must be filled with your personal info so the code can run
reddit = praw.Reddit(client_id = '',
					 client_secret = '',
					 user_agent = 'bot1',
					 username = '',
					 password = '')

subreddit = reddit.subreddit("learnpython")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
