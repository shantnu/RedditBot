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
#read in visite submissions as to avoid them
# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_logged.txt"):
    posts_logged = []
# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_logged.txt", "r") as f:
        posts_logged = f.read()
        posts_logged = posts_logged.split("\n")
        posts_logged = list(filter(None, posts_logged))
#read in old html as to save it
if not os.path.isfile("links.txt"):
    elm = []
# If we have run the code before, load the list of posts we have replied to
else:
    with open("links.txt", "r") as f:
        elm = f.read()
        elm = elm.split("\n")
        elm = list(filter(None, elm))

for s in subs:
    subreddit = reddit.subreddit(s)
    for submission in subreddit.rising(limit=5):
        #get comments and print relavent data
        #check if the submission has allready been checked
        if submission.id not in posts_logged:
            submission.comments.replace_more(limit=0)
            #add search in title and intext
            #
            #
            for comment in submission.comments.list():
                #search for the correct string
                if comment.body.find("the") != -1: #key word needs changed
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
                        # Store the current id into our list
                        posts_logged.append(submission.id)
                        break
print("---------------------------------\n")
# Write our updated list back to the file
with open("links.txt", "w") as f:
    for data in elm:
        f.write(data + "\n")
#Write visited back to text file
# Write our updated list back to the file
with open("posts_logged.txt", "w") as f:
    for post_id in posts_logged:
        f.write(post_id + "\n")
