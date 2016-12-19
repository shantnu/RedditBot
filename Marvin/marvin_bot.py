#!/usr/bin/python
import praw
import re
import random

# Quotes taken from: http://www.imdb.com/character/ch0007553/quotes
marvin_quotes = \
[
" I've calculated your chance of survival, but I don't think you'll like it. ",
" Do you want me to sit in a corner and rust or just fall apart where I'm standing?",
"Here I am, brain the size of a planet, and they tell me to take you up to the bridge. Call that job satisfaction? Cause I don't. ",
"Here I am, brain the size of a planet, and they ask me to pick up a piece of paper. ",
" It gives me a headache just trying to think down to your level. ",
" You think you've got problems. What are you supposed to do if you are a manically depressed robot? No, don't even bother answering. I'm 50,000 times more intelligent than you and even I don't know the answer.",
"Zaphod Beeblebrox: There's a whole new life stretching out in front of you. Marvin: Oh, not another one.",
"The first ten million years were the worst. And the second ten million... they were the worst too. The third ten million I didn't enjoy at all. After that, I went into a bit of a decline. ",
"Sorry, did I say something wrong? Pardon me for breathing which I never do anyway so I don't know why I bother to say it oh God I'm so depressed. ",
" I have a million ideas, but, they all point to certain death. ",

]

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("pythonforengineers")

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("Marvin Help", comment.body, re.IGNORECASE):
            marvin_reply = "Marvin the Depressed Robot says: " + random.choice(marvin_quotes)
            comment.reply(marvin_reply)
            print(marvin_reply)
            


