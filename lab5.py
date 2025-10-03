import RPi.GPIO as GPIO
import math
import time 


GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


pins = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
vals = [None] * len(pins)
fbase=0.2

but = 12


# generates sin wave based on pin (phase shift) and time
def singen():
	mat = [None] * len(pins)
	t = time.time()

	for pin in pins:
		mat[pin-2] = round(math.sin(2*math.pi*fbase*t - (pin-2)*math.pi/11) ** 2, 2)*100
	return mat



GPIO.setup(but, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


for pin in pins:
	GPIO.setup(pin, GPIO.OUT)
	
pwms = [GPIO.PWM(pin, fbase) for pin in pins]


i=0
for pwm in pwms:
	pwm.start(0)
	i+=1

try:
	while True:
		Bmat=singen()
		print(Bmat)

		for pin in pins:
			pwms[pin-2].ChangeDutyCycle(Bmat[pin-2])


		print('\n')

except KeyboardInterrupt:
	print('\nExiting')
finally:
	for pwm in pwms:
		pwm.stop()
	GPIO.cleanup()
	print("done")

GPIO.cleanup()

