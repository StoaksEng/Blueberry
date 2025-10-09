import RPi.GPIO as GPIO
import time
import shifter
import random

GPIO.setmode(GPIO.BCM)

dataPin, latchPin, clockPin = 23, 24, 25

GPIO.setup(dataPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial=0) # start latch & clock low
GPIO.setup(clockPin, GPIO.OUT, initial=0)

pattern = 0b01100110 # pattern to display

shift = shifter.Shifter(dataPin, clockPin, latchPin)

dir = 1

try:
	while 1:
		dir = random.randint(1, 2)
		shift.ShiftByte(dir)
		sleep(0.05)
		print("test")
except:
	GPIO.cleanup()
