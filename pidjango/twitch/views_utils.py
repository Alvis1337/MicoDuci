from pprint import pprint
from twitchAPI import Twitch, EventSub
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

twitch = Twitch(env('TWITCH_AUTH_CLIENT_ID'), env('TWITCH_AUTH_CLIENT_SECRET'))


async def user_authentication(data: dict):
    pprint(data)

TARGET_USERNAME = 'alvisleet'
WEBHOOK_URL = 'https://twitch.uttensio.com/callback/oauth'
APP_ID = env('TWITCH_AUTH_CLIENT_ID')
APP_SECRET = env('TWITCH_AUTH_CLIENT_SECRET')

twitch.authenticate_app([])

uid = twitch.get_users(logins=[TARGET_USERNAME])
user_id = uid['data'][0]['id']
# basic setup, will run on port 8080 and a reverse proxy takes care of the https and certificate
hook = EventSub(WEBHOOK_URL, APP_ID, 8080, twitch)
# unsubscribe from all to get a clean slate
hook.unsubscribe_all()
# start client
hook.start()
print('subscribing to hooks:')
hook.listen_channel_follow(user_id, on_follow)

try:
    input('press Enter to shut down...')
finally:
    hook.stop()
print('done')