# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import threading
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


def flashing_timeout():
    start_time = threading.Timer(6, control_led("off"))
    return start_time.start()


def albert():
    t = threading.currentThread()
    flashing_timeout()
    while getattr(t, "do_run", True):
        print(flashing_timeout())
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels)
            pixels[i] = wheel(pixel_index & 255)
            try:
                pixels.fill((0, 255, 0))
                pixels.show()
                time.sleep(1)

                pixels.fill((0, 0, 0))
                pixels.show()
                time.sleep(1)

                pixels.fill((255, 255, 0))
                pixels.show()
                time.sleep(1)

                print("in albert loop")

            except:
                return print("Failed to run the albert loop")
        init_led()
        print("init")
        print("terminating")


def fireball():
    t = threading.currentThread()
    flashing_timeout()
    while getattr(t, "do_run", True):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels)
            pixels[i] = wheel(pixel_index & 255)
            try:
                pixels.fill((255, 0, 0))
                pixels.show()
                time.sleep(1)

                pixels.fill((0, 0, 0))
                pixels.show()
                time.sleep(1)

                pixels.fill((255, 0, 0))
                pixels.show()
                time.sleep(1)

                print("in fireball loop")

            except:
                return print("Failed to run the fireball loop")
        init_led()
        print("init")
        print("terminating")


def hydrate():
    t = threading.currentThread()
    flashing_timeout()
    while getattr(t, "do_run", True):
        print('out?')
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels)
            pixels[i] = wheel(pixel_index & 255)
            try:
                # Comment this line out if you have RGBW/GRBW NeoPixels
                pixels.fill((0, 0, 255))
                # Uncomment this line if you have RGBW/GRBW NeoPixels
                # pixels.fill((255, 0, 0, 0))
                pixels.show()
                time.sleep(1)

                # Comment this line out if you have RGBW/GRBW NeoPixels
                pixels.fill((0, 0, 0))
                # Uncomment this line if you have RGBW/GRBW NeoPixels
                # pixels.fill((0, 255, 0, 0))
                pixels.show()
                time.sleep(1)

                # Comment this line out if you have RGBW/GRBW NeoPixels
                pixels.fill((0, 0, 255))
                # Uncomment this line if you have RGBW/GRBW NeoPixels
                # pixels.fill((0, 0, 255, 0))
                pixels.show()
                # print(j)
                print("in hydrate loop ")

                # self.hydrate(0.001)
            except:
                return print('Failed to run hydrate loop')
        init_led()
        return print("terminating")


def init_led():
    pixels.fill((250, 140, 160))
    pixels.show()


def control_led(pattern):
    target_func = ''
    if pattern == 'hydrate':
        target_func = hydrate()

    if pattern == 'fireball':
        target_func = fireball

    elif pattern == 'off':
        # enumerate currently running thraeds looking for led_loop thread
        for thread in threading.enumerate():
            # if we find an led_loop thread, tell it to kill itself
            if thread.name == 'led_loop':
                thread.do_run = False
                return None
    # if we reach this block, it's because we did not get a valid pattern, so raise relevant exception
    else:
        raise InvalidArgumentSupplied

    # create and start the control loop thread
    t = threading.Thread(name='led_loop', target=target_func, args=("task",))
    t.start()
