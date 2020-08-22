#!/usr/bin/env python
import configparser
import twitter
import pprint

config = configparser.ConfigParser()
config.read('credentials.ini')
credentials = config['CREDENTIALS']

api = twitter.Api(
    consumer_key=credentials['consumer_key'],
    consumer_secret=credentials['consumer_secret'],
    access_token_key=credentials['access_token_key'],
    access_token_secret=credentials['access_token_secret']
)

owned_lists = api.GetLists()

pprint.pprint(owned_lists)
