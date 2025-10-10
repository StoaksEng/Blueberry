import RPi.GPIO as GPIO
import time
import shifter
import random
import threading

GPIO.setmode(GPIO.BCM)

dataPin, latchPin, clockPin = 23, 24, 25

GPIO.setup(dataPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT, initial=0)  # start latch & clock low
GPIO.setup(clockPin, GPIO.OUT, initial=0)

pattern = 0b01100110  # pattern to display

shift = shifter.Shifter(dataPin, clockPin, latchPin)

led = 0b00010000


def randomStep(leds):
    try:
        bug = Bug()
        bug.start()

        while True:
            bug.start()   # starts blinking LEDs
            time.sleep(10)
            bug.stop()
            time.sleep(10)

    except Exception as e:
        print("Error:", e)
        GPIO.cleanup()


class Bug:
    def __init__(self, timeStep=0.1, x=3, isWrapOn=False):
        # composition: Bug "has a" Shifter
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

        # Move left (if possible)
        if move == -1:
            if self.x > 0 or self.isWrapOn:
                self.x -= 1

        # Move right (if possible)
        elif move == 1:
            if self.x < 7 or self.isWrapOn:
                self.x += 1

        led = 2 ** self.x
        self.shifter.shiftByte(led)

    def start(self):
        if not self.running:
            self.running = True
            self._thread = threading.Thread(target=self._run)
            self._thread.start()
            print("Bug started.")

    def stop(self):
        if self.running:
        	self.running = False
            self._thread.join()       # wait for thread to finish
            self.shifter.shiftByte(0)  # turn off all LEDs
            print("Bug stopped and LEDs off.")
