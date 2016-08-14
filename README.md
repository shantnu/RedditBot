SemiAmusingBot
==============

This is a fork of RedditBot
A simple Reddit bot in Python.

A software bot is a program that can interact with websites autonomously. They can be as simple or as complex as you want them to be.

The bot runs in the background and monitors a website. When it sees a change (like a post on Reddit), it can reply to it, upvote, or do any other task it was programmed to.


To learn how to build this bot, please see:

http://pythonforengineers.com/build-a-reddit-bot-part-1/

install.sh in Part 3 is for Unix installs.  For Windows installs, you will need to:
1. Install Python 2.7.12 (to avoid TLS errors you should have newest Python)
2. Install Pip for Windows
3. Install praw with pip
4. Download these scripts to run.

The bot now logs in using OAUTH. This requires some setup:
1. Copy praw_ini.sample to praw.ini
2. Visit Reddit and log in with the account that the bot will be running under.
3. Visit https://www.reddit.com/prefs/apps/
4. Click on the create another app button and fill in at least the app name.
	a. Fill in http://127.0.0.1:65010 for the redirect URI
5. Once you create the app - take the id# and the secret from the page and put this information in praw.ini along with the redirect URI.
6. You'll need to run get-secret.py.  
	a. It has a dependency - tornado - install that with pip
	b. If your bot will need different permissions - edit the line in get-secret.py that lists the permissions.
7. This will complete praw.ini with the last line of:
	oauth_refresh_token = <the token that authorizes you application>
	Fix it if the last line isn't the right format.
8. You can test the access by running test_access.py