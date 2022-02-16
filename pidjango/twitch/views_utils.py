from pprint import pprint

import twitch
from twitchAPI import Twitch
from twitch import TwitchHelix
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

client = twitch.TwitchHelix(env('TWITCH_AUTH_CLIENT_ID'), env('TWITCH_AUTH_CLIENT_SECRET'), scopes=[])


def user_authentication():
    oauth = client.get_oauth()
    pprint(oauth)
    pprint(client.get_streams())
