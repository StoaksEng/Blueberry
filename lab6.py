import RPi.GPIO as GPIO
import time
import shifter
import random
import threading

GPIO.setmode(GPIO.BCM)

dataPin, latchPin, clockPin = 23, 24, 25

GPIO.setup(dataPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial=0)
GPIO.setup(clockPin, GPIO.OUT, initial=0)

pattern = 0b01100110

shift = shifter.Shifter(dataPin, clockPin, latchPin)

led = 0b00010000



class Bug:
	def __init__(self, timeStep=0.1, x=3, isWrapOn=False):
		self.shifter = shifter.Shifter(dataPin, clockPin, latchPin)
		self.timeStep = timeStep
		self.x = x
		self.isWrapOn = isWrapOn
		self.running = False
		self._thread = None

	def _run(self):
		while self.running:
			self.randomStep()
			time.sleep(self.timeStep)

	def randomStep(self):
		move = random.choice([-1, 1])

		if move == -1:
			if self.x > 0:
				self.x -= 1
			elif self.isWrapOn:
				self.x = 8

		elif move == 1:
			if self.x < 7:
				self.x += 1
			elif self.isWrapOn:
				self.x = 0

		led = int(2 ** self.x)
		self.shifter.shiftByte(led)

	def start(self):
		if not self.running:
			self.running = True
			self._thread = threading.Thread(target=self._run)
			self._thread.start()
			print("Bug released.")

	def stop(self):
		if self.running:
			self.running = False
			self._thread.join()
			self.shifter.shiftByte(0)
			print("Bug squahsed.")


if __name__ == "__main__":
	try:
		bug = Bug()
		bug2=Bug(0.05, 1, True)
		while True:
			bug.start()
			time.sleep(10)
			bug.stop()
			print("Wraparound fast bug:")
			bug2.start()
			time.sleep(10)
			bug2.stop()
			print("Bug break time.")
			time.sleep(5)

	except KeyboardInterrupt:
		print("Stopping Program")
		bug.stop()
		bug2.stop()
		GPIO.cleanup()
		print("Program Stopped Safely")
