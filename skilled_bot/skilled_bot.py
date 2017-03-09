#!/usr/bin/python
import praw
import pdb
import re
import os
from praw.models import MoreComments

#track number of aded posts
added = 0
#create reddit instance
reddit = praw.Reddit('bot1')
#get the desired sub reddits
subs=["gaming", "modernmagic", "sports"]
#keyword to be used when searching
keyWord = "is"
#Have we run this code before? If not, create an empty list
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
if not os.path.isfile("links.php"):
    elm = []
# If we have run the code before, load the list of posts we have replied to
else:
    with open("links.php", "r") as f:
        elm = f.read()
        elm = elm.split("\n")
        elm = list(filter(None, elm))
        elm = list(reversed(elm))

for s in subs:
    subreddit = reddit.subreddit(s)
    for submission in subreddit.new(limit=5):
        #get comments and print relavent data
        #check if the submission has allready been checked
        if submission.id not in posts_logged:
            submission.comments.replace_more(limit=0)
            #add search in title and text
            #
            #
            for comment in submission.comments.list():
                #search for the correct string
                if comment.body.find(keyWord) != -1: #key word needs changed
                        title = submission.title
                        if len(title) > 55:
                            title = title[:len(title)-(len(title)-52)] +"..."
                        url = submission.url
                        cmt = comment.body
                        if len(cmt) > 13:
                            cmt = cmt[:len(cmt)-(len(cmt)-50)] +"..."
                        elm.append(str("<div class=\"rlink "+ s +"\"><div class=\"rinfo\"><span class=\"rtitle\"><a href=\""+url+"\">"+title+"</a></span><br /><span class=\"rtext\">"+cmt+"</span></div><div class=\"tag\"></div></div>"))
                        # Store the current id into our list
                        posts_logged.append(submission.id)
                        added = added + 1
                        break

print("added: "+str(added)+"\n---------------------------------\n")
elm=list(reversed(elm))
with open("links.php", "w") as f:
    for data in elm:
        f.write(data + "\n")
# update the file to make sure we dont double add links
with open("posts_logged.txt", "w") as f:
    for post_id in posts_logged:
        f.write(post_id + "\n")
