# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

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


class LedControl:
    def __init__(self):
        self.led_loop_control = None

    def wheel(self, pos):
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

    def rainbow_cycle(self, test):
        if self.led_loop_control:
            for j in range(255):
                for i in range(num_pixels):
                    pixel_index = (i * 256 // num_pixels) + j
                    pixels[i] = self.wheel(pixel_index & 255)
                    try:
                        # Comment this line out if you have RGBW/GRBW NeoPixels
                        pixels.fill((255, 0, 0))
                        # Uncomment this line if you have RGBW/GRBW NeoPixels
                        # pixels.fill((255, 0, 0, 0))
                        pixels.show()
                        time.sleep(1)

                        # Comment this line out if you have RGBW/GRBW NeoPixels
                        pixels.fill((0, 255, 0))
                        # Uncomment this line if you have RGBW/GRBW NeoPixels
                        # pixels.fill((0, 255, 0, 0))
                        pixels.show()
                        time.sleep(1)

                        # Comment this line out if you have RGBW/GRBW NeoPixels
                        pixels.fill((0, 0, 255))
                        # Uncomment this line if you have RGBW/GRBW NeoPixels
                        # pixels.fill((0, 0, 255, 0))
                        pixels.show()
                        time.sleep(1)
                        print(self.led_loop_control)

                        self.rainbow_cycle(0.001)
                    except:
                        return print('Failed to run cycle')


    def off_cycle(self):
        self.led_loop_control = False
        for j in range(255):
            for i in range(num_pixels):
                pixel_index = (i * 256 // num_pixels) + j
                pixels[i] = self.wheel(pixel_index & 255)

                # Uncomment this line if you have RGBW/GRBW NeoPixels
                pixels.fill((255, 0, 0, 0))
                pixels.show()

                # Uncomment this line if you have RGBW/GRBW NeoPixels
                pixels.fill((0, 255, 0, 0))
                pixels.show()

                # Uncomment this line if you have RGBW/GRBW NeoPixels
                pixels.fill((0, 0, 255, 0))
                pixels.show()

    def control_led(self, pattern):
        if pattern == 'rainbow':
            print('doing the rainbow cycle')
            self.led_loop_control = True
            self.rainbow_cycle(pattern)

        elif pattern == 'off':
            self.off_cycle()
        #     static color
