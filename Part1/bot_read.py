#!/usr/bin/python
import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("modernmagic")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    linkData = submission.url
    print("Url: ", linkData)    
    print("---------------------------------\n")
