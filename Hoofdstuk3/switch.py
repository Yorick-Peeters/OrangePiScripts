import time
import wiringpi
import sys
#SETUP
print ("Start")
pinLed = 2
pinSwitch = 1
wiringpi.wiringPiSetup() 
wiringpi.pinMode (pinLed, 1) 
wiringpi.pinMode (pinSwitch, 0)
#infinite loop stop using CTRL-C Ewhile True:
while True:
    if (wiringpi.digitalRead(pinSwitch) == 0):
        print("Button pressed")
        time.sleep(0.3)
        wiringpi.digitalWrite(pinLed, 1)
    else:
        print("Button released")
        time.sleep(0.3)
        wiringpi.digitalWrite(pinLed, 0)