#!/usr/bin/env python2.7

import datetime
import oauth2
import sys
import urllib

try:
    from twitter_api_keys import *
except ImportError:
    sys.exit('You need to fill out twitter_api_keys.py')


def oauth_req(url, http_method='GET', post_body='', http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=ACCESS_TOKEN, secret=ACCESS_TOKEN_SECRET)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
    return content


# Post a status to the timeline
status = datetime.date.today().strftime('--- %Y-%m-%d, %A ---')
response = oauth_req('https://api.twitter.com/1.1/statuses/update.json?' + urllib.urlencode({'status': status}), http_method='POST')
assert 'id' in response
