#!/usr/bin/env python
import configparser
import twitter
import pprint

config = configparser.ConfigParser()
config.read('credentials.ini')
api = twitter.Api(**config['CREDENTIALS'])

# owned_lists = api.GetLists()
# pprint.pprint(owned_lists)

# user = api.GetUser(screen_name="_cryptoanarchy")


# for user in api.GetFriends():
#     # for user in [user]:
#     if user.status is not None and user.status.created_at_in_seconds < 1564617600:
#         pprint.pprint(user)
#         print("Last Status At:", user.status.created_at_in_seconds)
#         print("============================")


for screen_name in screen_names:
    # pprint.pprint(user)
    # pprint.pprint(user.description)
    # print("====================")
    print(screen_name)
    api.DestroyFriendship(screen_name=screen_name)
    api.CreateListsMember(screen_name=screen_name,
                          list_id=1297270043580026880)
