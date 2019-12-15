from christmastree import ChristmasTree
from gpiozero.tools import random_values
from time import sleep
from signal import pause

def fwd_on(leds):
    for led in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        leds[led].on()
        sleep(.2)   
def rev_on(leds):
    for led in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
        leds[led].on()
        sleep(.2)
def fwd_off(leds):
    for led in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        leds[led].off()
        sleep(.2)   
def rev_off(leds):
    for led in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
        leds[led].off()
        sleep(.2)       
def reds_on(leds):
    for led in [1, 3, 4, 6, 8]:
        leds[led].on()
def greens_on(leds):
    for led in [0, 2, 5, 7, 9]:
        leds[led].on()
def redants_on(leds):
    for led in [1, 3, 4, 6, 8]:
        leds[led].on()
        sleep(.2)
def greenants_on(leds):
    for led in [0, 2, 5, 7, 9]:
        leds[led].on()
        sleep(.2)
def redants_off(leds):
    for led in [1, 3, 4, 6, 8]:
        leds[led].off()
        sleep(.2)
def greenants_off(leds):
    for led in [0, 2, 5, 7, 9]:
        leds[led].off()
        sleep(.2)        
def bottom_on(leds):
    for led in [0, 1, 2, 3]:
        leds[led].on()
def mid_on(leds):
    for led in [4, 5, 6, 7]:
        leds[led].on()
def top_on(leds):
    for led in [8, 9]:
        leds[led].on()
def bottom_off(leds):
    for led in [0, 1, 2, 3]:
        leds[led].off()
def mid_off(leds):
    for led in [4, 5, 6, 7]:
        leds[led].off()
def top_off(leds):
    for led in [8, 9]:
        leds[led].off()
def random(leds):
    for led in leds:
		led.source_delay = 0.1
		led.source = random_values()
	sleep(5)
except:
	tree.off()

tree = ChristmasTree(pwm=True)
leds = tree.leds

try:
    tree.star.off()
    while True:
        fwd_on(leds)
        sleep(.5)
        tree.off()
        sleep(.5)
        tree.on()
        sleep(.5)
        tree.off()
        sleep(.5)
        tree.baubles.off()
        rev_on(leds)
        sleep(.5)
        tree.off()
        sleep(.5)
        tree.on()
        sleep(.5)
        tree.off()
        sleep(.5)
        tree.star.on()
        tree.baubles.off()
        reds_on(leds)
        sleep(.5)
        tree.baubles.off()
        greens_on(leds)
        sleep(.5)
        tree.baubles.off()
        reds_on(leds)
        sleep(.5)
        tree.baubles.off()
        greens_on(leds)
        sleep(.5)
        tree.off()
        sleep(.5)
        tree.on()
        sleep(.5)
        tree.off()
        sleep(.5)
        bottom_on(leds)
        sleep(.5)
        mid_on(leds)
        sleep(.5)
        top_on(leds)
        sleep(.5)
        tree.star.on()
        sleep(.5)
        tree.off()
        sleep(.5)
        tree.on()
        sleep(.5)
        tree.off()
        sleep(.5)
        tree.star.on()
        sleep(.5)
        top_on(leds)
        sleep(.5)
        mid_on(leds)
        sleep(.5)
        bottom_on(leds)
        sleep(.5)
        tree.star.off()
        sleep(.5)
        top_off(leds)
        sleep(.5)
        mid_off(leds)
        sleep(.5)
        bottom_off(leds)
        sleep(.5)
        tree.on()
        sleep(.5)
        tree.off()
        sleep(.5)
        tree.on()
        sleep(.5)
        fwd_off(leds)
        sleep(.5)
        tree.on()
        sleep(.5)
        tree.off()
        sleep(.5)
        tree.on()
        sleep(.5)
        rev_off(leds)
        sleep(.5)
        tree.on()
        sleep(.5)
        tree.off()
        sleep(.5)
        redants_on(leds)
        sleep(.01)
        greenants_on(leds)
        sleep(.01)
        tree.star.on()
        sleep(.5)
        tree.off()
        sleep(.5)
        tree.on()
        sleep(.5)
        tree.off()
        sleep(.5)
        tree.on()
        sleep(.5)
        greenants_off(leds)
        sleep(.01)
        redants_off(leds)
        sleep(.01)
        tree.star.off()
        sleep(.5)
        tree.on()
        sleep(.5)
        tree.off()
        sleep(.5)
        random(leds)
        sleep(.5)
        tree.off()
        sleep(.5)
        tree.on()
        sleep(.5)
        
except:
        tree.star.on()
