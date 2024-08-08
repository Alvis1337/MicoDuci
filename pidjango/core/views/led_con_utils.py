import threading
import time
import board
import neopixel

pixel_pin = board.D18

num_pixels = 60
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=1, auto_write=False, pixel_order=ORDER
)


def init_led():
    pixels.fill((255, 50, 80))
    pixels.show()

def sweep():
    for i in range(len(pixels)):
        pixels[i] = (255, 50, 80)
        time.sleep(0.05)
        pixels.show()
    for i in range(len(pixels)):
        pixels[i] = (0, 0, 0)  # Turn off
        time.sleep(0.05)
        pixels.show()

def alternate():
    for i in range(len(pixels)):
        if i % 2 == 0:
            pixels[i] = (0, 255, 0)  # Green color
        else:
            pixels[i] = (0, 0, 255)  # Blue color
    pixels.show()
    time.sleep(1)
    pixels.fill((0, 0, 0))  # Turn off
    pixels.show()

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

def animate_pixels(color):
    print('starting')

    for i in range(5):
        pixel_index = (i * 256 // num_pixels)
        pixels[i] = wheel(pixel_index & 255)
        pixels.fill(color)
        pixels.show()
        time.sleep(1)

        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(1)

        pixels.fill(color)
        pixels.show()
        time.sleep(1)
    sweep()
    init_led()


def albert():
    animate_pixels((0, 255, 0))

def fireball():
    animate_pixels((255, 0, 0))


def hydrate():
   animate_pixels((0, 0, 255))

def wheel_spin():
   animate_pixels((255, 255, 0))

def hero_request():
   animate_pixels((0, 204, 255))

def mod_poll():
    animate_pixels((255, 102, 0))

def tarot_reading():
    animate_pixels((128, 0, 128))
        

def lose_glasses_5():
    animate_pixels((255, 255, 255))

def control_led(pattern):
    pattern_functions = {
        'hydrate': hydrate,
        'fireball': fireball,
        'albert': albert,
        'wheel-spin': wheel_spin,
        'hero_request': hero_request,
        'mod_poll': mod_poll,
        'tarot_reading': tarot_reading,
        'lose_glasses_5': lose_glasses_5
    }

    if pattern in pattern_functions:
        t1 = threading.Thread(name='led_loop', target=pattern_functions[pattern])
        t2 = threading.Thread(target=init_led)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    if pattern == 'off':
        return init_led()
    else:
        print(f"Pattern '{pattern}' not recognized.")
    
