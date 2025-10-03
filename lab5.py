import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


ports = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
but = 12
pwms = [None] * len(ports)
fbase = 500

GPIO.setup(but, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


for i in range(len(ports)):
	GPIO.setup(ports[i], GPIO.OUT, initial=0)
	print(i)

for i in range(len(ports)):
	pwms[i] = GPIO.PWM(ports[i], fbase)
	# pwms[i].start(10*i)

try:
	while 1:
		print("ping")
		sleep(1)
except KeyboardInterrupt:
	print('\nExiting')
except Exception as e:
	print('\ne')

GPIO.cleanup()

