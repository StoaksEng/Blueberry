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

	move = random.choice([-1, 1])
	# Move left
	if move == -1 and leds < 0b10000000:
		leds <<= 1
	# Move right
	elif move == 1 and leds > 0b00000001:
		leds >>= 1
		# If at edge, reverse direction
	return leds

try:
	while True:
		led = randomStep(led)
		print("sending:")
		print(format(led, '08b'))
		shift.shiftByte(led)
		print("test2")
		time.sleep(0.05)
except Exception as e:
    print("Error:", e)
    GPIO.cleanup()
