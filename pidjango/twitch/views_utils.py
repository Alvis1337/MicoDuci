from twitchAPI import AuthScope, UserAuthenticator
from twitchAPI.twitch import Twitch
import environ


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

twitch = Twitch(env('TWITCH_AUTH_CLIENT_ID'), env('TWITCH_AUTH_CLIENT_SECRET'))


def user_authentication():
    target_scope = [AuthScope.CHANNEL_READ_REDEMPTIONS]
    callback = env('APP_URL') + ':17563'
    auth = UserAuthenticator(twitch, target_scope, force_verify=False)
    # this will open your default browser and prompt you with the twitch verification website
    token, refresh_token = auth.authenticate()
    # add User authentication
    twitch.set_user_authentication(token, target_scope, refresh_token)
