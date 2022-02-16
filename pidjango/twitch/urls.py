from django.urls import path
from .views import UserAuthenticationView

app_name = 'twitch'

urlpatterns = [
    path('user-auth/', UserAuthenticationView.as_view(), name='user-auth'),
]
