import RPi.GPIO as GPIO
import time

DELAY_ON = 5
DELAY_OFF = 30
IN1 = 16
  
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IN1, GPIO.OUT)

try:

 while True:
        print("Turning on")
 	GPIO.output(IN1, True)
 	time.sleep(DELAY_ON)
        print("Turning off")
 	GPIO.output(IN1, False)
 	time.sleep(DELAY_OFF)

except KeyboardInterrupt:
	GPIO.cleanup()
