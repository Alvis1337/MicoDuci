import http

from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.views import APIView
from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope
import environ
from .views_utils import user_authentication
from django.http import JsonResponse

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

twitch = Twitch(env('TWITCH_AUTH_CLIENT_ID'), env('TWITCH_AUTH_CLIENT_SECRET'))


class UserAuthenticationView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        user_authentication()
        return JsonResponse({"result": "very good:)"}, status=status.HTTP_200_OK)
