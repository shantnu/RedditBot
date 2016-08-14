#!/usr/bin/env python
'''
So I heard you want to use OAuth2? This is a helper tool that gets the
authenticaton code for you and fires it into praw.ini.

How to use:
    - Visit: https://www.reddit.com/prefs/apps
    - Create new "script", under "redirect uri" put http://127.0.0.1:65010
    - Open praw.ini
        - oauth_client_id = { The ID displayed under the icon thingy }
        - oauth_client_secret = { The secret }
        - oauth_redirect_uri = http://127.0.0.1:65010
    - Run this script
    - Your browser will open to a page on Reddit listing requested perms
    - Click permit
'''

import praw
import webbrowser
from warnings import warn
from praw.errors import HTTPException, OAuthAppRequired
from tornado import gen, web
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer

r = praw.Reddit('Shreddit refresh token grabber')


class Page(web.RequestHandler):
    def get(self):
        code = self.get_argument("code", default=None, strip=False)
        self.write("Success! Your code: %s<br> \
        It will now be appended to praw.ini and you \
                should be able to enjoy Shreddit without storing \
                your user / pass anywhere." % code)
        IOLoop.current().stop()
        self.login(code)

    def login(self, code):
        deets = r.get_access_information(code)
        print("oauth_refresh_token: %s" % deets['refresh_token'])
        r.set_access_credentials(**deets)
        with open('praw.ini', mode='a') as fh:
            fh.write('oauth_refresh_token = %s' % deets['refresh_token'])
            print("Refresh token written to praw.ini")

application = web.Application([(r"/", Page)])

try:
    r.refresh_access_information()
except HTTPException:
    url = r.get_authorize_url('uniqueKey', ['identity', 'read', 'submit', 'vote', 'edit', 'history'], True)
    try:
        print("Opening url: %s" % url)
        webbrowser.open(url, new=2)
    except NameError:
        warn('''Couldn't open URL: %s\n please do so manually''' % url)
    server = HTTPServer(application)
    server.listen(65010)
    IOLoop.current().start()

if r.user == None:
    print("Failed to log in. Something went wrong!")
else:
    print("Logged in as %s." % r.user)

print()
