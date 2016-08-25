#!/usr/bin/env python
'''
Simple script to check if your oauth is working.
'''
import praw
import sys

r = praw.Reddit('SemiAmusingBot oauth test')
r.refresh_access_information()
if r.is_oauth_session():
    print "Success"
    sys.exit(0)
else:
    print "Fail"
    sys.exit(2)
