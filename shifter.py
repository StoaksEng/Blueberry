import RPi.GPIO as GPIO
import time

byte = 1

class Shifter:
    def __init__(self, serialPin, clockPin, latchPin):
        self.serialPin = serialPin
        self.clockPin = clockPin
        self.latchPin = latchPin

    def _ping(self, p):
        GPIO.output(p,1)
        time.sleep(0)
        GPIO.output(p,0)

    def shiftByte(self, b):
        print("recieving:")
        print(format(b, '08b'))
        for i in range(8):
            GPIO.output(self.serialPin, b & (1<<i))
            ping(self.clockPin) # add bit to register
        ping(self.latchPin) # send register to output
