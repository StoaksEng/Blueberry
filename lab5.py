import RPi.GPIO as GPIO
from time import sleep
from time import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

pins = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
but = 12
fbase = 500

GPIO.setup(but, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


for pin in pins
	GPIO.setup(pin, GPIO.OUT)
	
pwms = [GPIO.PWM(pin, fbase) for pin in pins]


i=0;

for pwm in pwms:
	pwm.start(i*pi/11)
	i+=1

try:
	print("PWM objects initialized. Running for 10 seconds...")
	sleep(10)
except KeyboardInterrupt:
	print('\nExiting')
except Exception as e:
	print('\ne')
finally:
	for pwm in pwms:
		pwm.stop()
	GPIO.cleanup()
	print("done")

