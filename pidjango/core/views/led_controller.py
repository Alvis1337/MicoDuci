from django.http import JsonResponse
from rest_framework import status, permissions
from rest_framework.views import APIView
from ..exceptions import NoArgumentSupplied, InvalidArgumentSupplied

from .led_con_utils import control_led


class ControlLED(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        pattern = request.POST.get('blink_pattern')
        arg_list = ['test', 'hydrate', 'off']
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

