#!/usr/bin/python
import praw

user_agent = ("SemiAmusingBot 0.16")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("pythonforengineers")

for submission in subreddit.get_hot(limit = 5):
    print "Title: ", submission.title
    print "Text: ", submission.selftext
    print "Score: ", submission.score
    print "Submission ID: ", submission.id
    print "---------------------------------\n"
