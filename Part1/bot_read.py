#!/usr/bin/python
import praw
import pdb
import re
import os
from praw.models import MoreComments

#create reddit instance
reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("modernmagic")
elm=[]

for submission in subreddit.hot(limit=5):
    #get comments and print relavent data
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        if comment.body.find("the") != -1:
                title = submission.title
                score = submission.score
                url = submission.url
                cmt = comment.body
                if len(cmt) > 13:
                    cmt = cmt[:len(cmt)-10] +"..."
                elm.append(str("<div class=\"rlink\"><img src=\"rlogo.jpg\" alt=\"link or default reddit icon\" /><div class=\"rinfo\"><span class=\"rtitle\">"+title+"</span><br /><span class=\"rtext\">"+cmt+"</span></div><div class=\"points\">"+str(score)+"</div></div>"))
                break
    print("---------------------------------\n")
# Write our updated list back to the file
with open("test.txt", "w") as f:
    for data in elm:
        f.write(data + "\n")
