#!/usr/bin/python
import praw
import pdb
import re
import os
import sys
from config_bot import *

# Check that the file that contains our username exists
if not os.path.isfile("config_bot.py"):
    print "You must create a config file with your username and password."
    print "Please see config_skel.py"
    exit(1)

# Create the Reddit instance
user_agent = ("SemiAmusingBot 0.2")
r = praw.Reddit(user_agent=user_agent)

# and login (DON'T USE THIS AGAIN)
#r.login(REDDIT_USERNAME, REDDIT_PASS)
r.refresh_access_information()
# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = filter(None, posts_replied_to)

# Get the top 5 values from our subreddit
subreddit = r.get_subreddit('pythonforengineers')

f = open("posts_replied_to.txt","a")
for submission in subreddit.get_hot(limit=50):
    # print submission.title

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("i love python", submission.title, re.IGNORECASE):
            # Reply to the post
            try:
                submission.add_comment("SemiAmusingBot says: They're very gentle snakes.")
            except:
		print "Error: ", sys.exc_info()[0]
                print "Probably rate limited cuz you're a bot."
                f.close()
                quit()
            else:
                print "Bot replying to : ", submission.title
                # write these out as we go so if we get rate limited, we have the data 
                f.write(submission.id + "\n")
      
                # Store the current id into our list
                posts_replied_to.append(submission.id)

# Close out the submissions replied to
f.close()