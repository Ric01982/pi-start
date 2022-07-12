import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

while True:
    pirdetection = GPIO.input(11)
    if pirdetection == 0:
        print("no movement")
    if pirdetection == 1:
        print("movement")
    time.sleep(0.1)


