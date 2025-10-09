import RPi.GPIO as GPIO
import time
import shifter

GPIO.setmode(GPIO.BCM)

dataPin, latchPin, clockPin = 23, 24, 25

GPIO.setup(dataPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial=0) # start latch & clock low
GPIO.setup(clockPin, GPIO.OUT, initial=0)

pattern = 0b01100110 # pattern to display

shift = shifter.Shifter(dataPin, clockPin, latchPin)

try:
	while 1:
		for i in range(2**8):
			shift.shiftByte(i)
			time.sleep(0.5)
except:
	GPIO.cleanup()
