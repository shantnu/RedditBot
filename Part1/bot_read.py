#!/usr/bin/python
import praw
import pdb
import re
import os
from praw.models import MoreComments

#create reddit instance
reddit = praw.Reddit('bot1')
#get the desired sub reddits
subs=["gaming"]
#all the html will be stored here
elm=[]
vsd=[]
#read in visite submissions as to avoid them
#
#
#read in old html as to save it
#
#



for s in subs:
    subreddit = reddit.subreddit(s)
    for submission in subreddit.hot(limit=5):
        #get comments and print relavent data
        #check if the submission has allready been checked
        #
        #
        #if not add it to the list
        #
        #
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            #search for the correct string
            if comment.body.find("the") != -1:
                    title = submission.title
                    if len(title) > 55:
                        title = title[:len(title)-(len(title)-52)] +"..."
                    score = submission.score
                    if score > 10000:
                        score = str(score%1000) + "k"
                    url = submission.url
                    cmt = comment.body
                    if len(cmt) > 13:
                        cmt = title[:len(cmt)-(len(cmt)-50)] +"..."
                    elm.append(str("<div class=\"rlink\"><img src=\"rlogo.jpg\" alt=\"link or default reddit icon\" /><div class=\"rinfo\"><span class=\"rtitle\">"+title+"</span><br /><span class=\"rtext\">"+cmt+"</span></div><div class=\"points\">"+str(score)+"</div></div>"))
                    break
print("---------------------------------\n")
# Write our updated list back to the file
with open("test.txt", "w") as f:
    for data in elm:
        f.write(data + "\n")
#Write visited back to text file
