#!/usr/bin/python
import praw

user_agent = ("PyFor Eng bot 0.1")
r = praw.Reddit(user_agent=user_agent)

subreddit = r.get_subreddit('python')

for submission in subreddit.get_hot(limit=5):
    print submission.title
    print submission.selftext
    print submission.score

subreddit = r.get_subreddit('learnpython')

for submission in subreddit.get_hot(limit=5):
    print submission.title
    print submission.selftext
    print submission.score
