# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import threading
import concurrent.futures
import time
import board
import neopixel
from ..exceptions import InvalidArgumentSupplied

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
from django.http import JsonResponse
from rest_framework import status

pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 6
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def albert():
    print('starting')

    for i in range(num_pixels):
        pixel_index = (i * 256 // num_pixels)
        pixels[i] = wheel(pixel_index & 255)
        pixels.fill((0, 255, 0))
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 255, 0))
        pixels.show()
        time.sleep(1)


def fireball():
    print('starting')

    for i in range(num_pixels):
        pixel_index = (i * 256 // num_pixels)
        pixels[i] = wheel(pixel_index & 255)
        pixels.fill((255, 0, 0))
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(1)

        pixels.fill((255, 0, 0))
        pixels.show()
        time.sleep(1)


def hydrate():
    print('starting')

    for i in range(num_pixels):
        pixel_index = (i * 256 // num_pixels)
        pixels[i] = wheel(pixel_index & 255)
        pixels.fill((0, 0, 255))
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 0, 255))
        pixels.show()
        time.sleep(1)

        print("in hydrate loop")

def wheel_spin():
    print('starting')

    for i in range(num_pixels):
        pixel_index = (i * 256 // num_pixels)
        pixels[i] = wheel(pixel_index & 255)
        pixels.fill((255, 255, 0))
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(1)

        pixels.fill((255, 255, 0))
        pixels.show()
        time.sleep(1)

        print("in hydrate loop")

def hero_request():
    print('starting')

    for i in range(num_pixels):
        pixel_index = (i * 256 // num_pixels)
        pixels[i] = wheel(pixel_index & 255)
        pixels.fill((0, 204, 255))
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 204, 255))
        pixels.show()
        time.sleep(1)

        print("in hydrate loop")

def mod_poll():
    print('starting')

    for i in range(num_pixels):
        pixel_index = (i * 256 // num_pixels)
        pixels[i] = wheel(pixel_index & 255)
        pixels.fill((255, 102, 0))
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(1)

        pixels.fill((255, 102, 0))
        pixels.show()
        time.sleep(1)

        print("in hydrate loop")

def tarot_reading():
    print('starting')

    for i in range(num_pixels):
        pixel_index = (i * 256 // num_pixels)
        pixels[i] = wheel(pixel_index & 255)
        pixels.fill((128, 0, 128))
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(1)

        pixels.fill((128, 0, 128))
        pixels.show()
        time.sleep(1)

        print("in hydrate loop")

def lose_glasses_5():
    print('starting')

    for i in range(num_pixels):
        pixel_index = (i * 256 // num_pixels)
        pixels[i] = wheel(pixel_index & 255)
        pixels.fill((255, 255, 255))
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(1)

        pixels.fill((255, 255, 255))
        pixels.show()
        time.sleep(1)

        print("in hydrate loop")


def init_led():
    pixels.fill((250, 140, 160))
    pixels.show()


def kill_thread():
    print('sleeping')
    time.sleep(6)
    for thread in threading.enumerate():
        # if we find an led_loop thread, tell it to kill itself
        thread.do_run = False
        return


def control_led(pattern):
    t2 = threading.Thread(target=kill_thread())
    if pattern == 'hydrate':
        t1 = threading.Thread(name='led_loop', target=hydrate())
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        init_led()
    if pattern == 'fireball':
        t1 = threading.Thread(name='led_loop', target=fireball())
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        init_led()
    if pattern == 'albert':
        t1 = threading.Thread(name='led_loop', target=albert())
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        init_led()
    if pattern == 'wheel-spin':
        t1 = threading.Thread(name='led_loop', target=wheel_spin())
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        init_led()
    if pattern == 'hero-request':
        t1 = threading.Thread(name='led_loop', target=hero_request())
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        init_led()
    if pattern == 'mod-poll':
        t1 = threading.Thread(name='led_loop', target=mod_poll())
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        init_led()
    if pattern == 'tarot-reading':
        t1 = threading.Thread(name='led_loop', target=tarot_reading())
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        init_led()
    if pattern == 'lose-glasses-5':
        t1 = threading.Thread(name='led_loop', target=lose_glasses_5())
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        init_led()
