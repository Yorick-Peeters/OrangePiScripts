import time
import wiringpi
import sys

def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)    # Write 1 ( HIGH ) to pin
    time.sleep(0.01)
    wiringpi.digitalWrite(_pin, 0)    # Write 1 ( HIGH ) to pin
    time.sleep(0.01)

#SETUP
print("Start")
pin4 = 4
pin8 = 8
pin10 = 10
pin12 = 12
# Set pin to mode 1 ( OUTPUT )

#MAIN
gpio.init()
gpio.setmode(gpio.BOARD)
gpio.setup(pin4, gpio.OUT)
gpio.setup(pin8, gpio.OUT)
gpio.setup(pin10, gpio.OUT)
gpio.setup(pin12, gpio.OUT)

#cleanup
print("Done")