import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


ports = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
but = 12
pwms = []
fbase = 500

GPIO.setup(but, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


for i in range(9):
	GPIO.setup(ports[i], GPIO.OUT, initial=0)
	pwms.append(GPIO.PWM(ports[i], fbase))

	pwms[i].start(10*i)

try:
	print("ping")
	sleep(1)
except KeyboardInterrupt:
	print('\nExiting')
except Exception as e:
	print('\ne')

GPIO.cleanup()

