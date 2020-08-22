#!/usr/bin/env python
import configparser
import twitter
import pprint

config = configparser.ConfigParser()
config.read('credentials.ini')
api = twitter.Api(**config['CREDENTIALS'])

# owned_lists = api.GetLists()
# pprint.pprint(owned_lists)

user = api.GetUser(screen_name="_cryptoanarchy")

# for user in api.GetFriends():
for user in [user]:
    pprint.pprint(user)
    print("Last Status At:", user.status.created_at)
    print("============================")
