import RPi.GPIO as GPIO
import time

byte = 1

class Shifter:
    def __init__(self, serialPin, clockPin, latchPin):
        self.serialPin = serialPin
        self.clockPin = clockPin
        self.latchPin = latchPin

    def _ping(p):
        GPIO.output(p,1)
        time.sleep(0)
        GPIO.output(p,0)

    def shiftByte(b):
        print(format(b, '08b'))
        for i in range(8):
            GPIO.output(dataPin, b & (1<<i))
            self.ping(clockPin) # add bit to register
        self.ping(latchPin) # send register to output
