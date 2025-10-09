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

led = 0b00010000 

def randomStep(leds):
	print(format(leds, '08b'))
	move = random.choice([-1, 1])
	# Move left
	if move == -1 and leds < 0b10000000:
		leds <<= 1
	# Move right
	elif move == 1 and leds > 0b00000001:
		leds >>= 1
		# If at edge, reverse direction
	else:
		leds = leds  # stay put or could reverse
	sleep(1)
	print(format(leds, '08b'))
	sleep(1)
	return leds

try:
	while True:
		led = randomStep(led)
		print("test1")
		shift.ShiftByte(led)
		print("test2")
		sleep(0.05)
		print("test3")

except:
	GPIO.cleanup()
