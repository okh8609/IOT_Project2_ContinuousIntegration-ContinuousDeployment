#!/bin/python3
import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    print("OK")

def blink():
    while True:
        # GPIO.output(11,GPIO.HIGH)
        # time.sleep(1.5)
        # GPIO.output(11,GPIO.LOW)
        # time.sleep(1.5)
        GPIO.output(11,GPIO.HIGH)
        time.sleep(0.08)
        GPIO.output(11,GPIO.LOW)
        time.sleep(0.08)

if __name__=="__main__":
    setup()
    blink()
