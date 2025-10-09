import RPi.GPIO as GPIO
import time

int byte

class Shifter:
    def __init__(self, serialPin, clockPin, latchPin):
        self.serialPin = serialPin
        self.clockPin = clockPin
        self.latchPin = latchPin

    def _ping(p)
        GPIO.output(p,1)
        time.sleep(0)
        GPIO.output(p,0)

    def shiftByte(b)

        if b == 1 && b < 8:
            b+=1
        else if b == 2 && b > 0
            b-=1

        for i in range(8):
            GPIO.output(dataPin, b & (1<<i))
            self.ping(clockPin) # add bit to register
            self.ping(latchPin) # send register to output
