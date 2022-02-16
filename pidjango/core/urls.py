from django.contrib import admin
from django.urls import path
# from pidjango.core.views.led_controller import ControlLED

urlpatterns = [
#    path('blink-api/', ControlLED.as_view(), name='blink-pattern')
    path('blink-api/', 'hi')
]
