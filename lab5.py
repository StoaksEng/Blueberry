import RPi.GPIO as GPIO
import math
import time 


GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#gpio output pin assignments
pins = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#gpio input pin assignment
but = 12
#empty list of values created for editing
vals = [None] * len(pins)
#sin wave frequency
f=0.2
#pwm base frequency
fbase=500
#initial 'forward' set of direction variable
direc = 1

#reverses direction of scroll
def rev(pin):
	global direc
	direc *= -1
	print("rev")

# generates absolute (positive values only) sin wave based on pin (phase shift) and time
def singen():
	mat = [None] * len(pins)
	t = time.time()
	#assign wave values to all pins
	for pin in pins:
		mat[pin-2] = round(math.sin(2*math.pi*f*t - direc * (pin-2)*math.pi/11) ** 2, 2)*100
	return mat

#setup input pin for reading
GPIO.setup(but, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#event detector to switch direction of sin wave
GPIO.add_event_detect(but, GPIO.RISING, callback=rev, bouncetime=100)

#setup output pins
for pin in pins:
	GPIO.setup(pin, GPIO.OUT)
	
#list comprehensive assignment/creation of pwms
pwms = [GPIO.PWM(pin, fbase) for pin in pins]

#startup pwm objects
for pwm in pwms:
	pwm.start(0)

try:
	#calls singen function to generate values, then assigns the values in a for loop
	while True:
		Bmat=singen()
		for pin in pins:
			pwms[pin-2].ChangeDutyCycle(Bmat[pin-2])
#escape exception handling
except KeyboardInterrupt:
	print('\nExiting')
finally:
	#GPIO cleanup
	for pwm in pwms:
		pwm.stop()
	GPIO.cleanup()
	print("done")
