from pprint import pprint
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from ..exceptions import NoArgumentSupplied, InvalidArgumentSupplied
from .led_con_utils import control_led
from twitchAPI.twitch import Twitch
from twitchAPI import EventSub


def callback_user_changed(uuid, data):
    print('Callback User changed for UUID ' + str(uuid))
    pprint(data)


def twitchwebhook(arg):
    target_username = 'uttensio'
    webhook_url = 'https://camphelp.ngrok.io/oauth/callback'
    app_id = 'fpdbev7ktti34dhr9cwpbxa17tfqc6'
    app_secret = 'd3va2j8wk5ui61oj63ljksvta14vfn'

    twitch = Twitch(app_id, app_secret)
    twitch.authenticate_app([])

    uid = twitch.get_users(logins=[target_username])
    user_id = uid['data'][0]['id']
    # basic setup, will run on port 8080 and a reverse proxy takes care of the https and certificate
    hook = EventSub(webhook_url, app_id, 8080, twitch)
    # unsubscribe from all to get a clean slate
    hook.unsubscribe_all()
    # start client
    hook.start()
    print('subscribing to hooks:')
    hook.listen_channel_points_custom_reward_redemption_add(user_id)

    try:
        input('press Enter to shut down...')
    finally:
        hook.stop()
    print('done')


#
class ControlLED(APIView):

    def post(self, request):
        pattern = request.POST.get('blink_pattern')
        arg_list = ['fireball', 'hydrate', 'off']
        # verify we have recieved a valid parameter else raise exception
        if not pattern:
            raise NoArgumentSupplied
        if pattern not in arg_list:
            raise InvalidArgumentSupplied
        print(pattern)

        # blink LEDs
        try:
            control_led(pattern)
            return JsonResponse({"data": pattern + " is the pattern"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return JsonResponse({"error": "big problem lol"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
