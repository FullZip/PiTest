import RPi.GPIO as GPIO
import time 


# BCM Number of LED indicators
leds = [5, 6, 13, 19]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for i in range(len(leds)):
    GPIO.setup(leds[i], GPIO.OUT)



try:
    while True:
	for led in leds:
       	    GPIO.output(led, GPIO.HIGH)
	    time.sleep(0.01)
            GPIO.output(led, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("BYE")
