import RPi.GPIO as GPIO
import time

DIR = 0
STEP = 0

#clockwise/countercw
cwise = 1
ccwise = 0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, cwise)

try:
    while True:
        time.sleep(1)
        GPIO.output(DIR, cwise)
        for a in range(500):
            GPIO.output(STEP, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(STEP, GPIO.LOW)
            time.sleep(1)
        time.sleep(1)
        GPIO.output(DIR, ccwise)
        for a in range(500):
            GPIO.output(STEP, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(STEP, GPIO.LOW)
            time.sleep(1)
        
except KeyboardInterrupt:
    print("bersihkan")
    GPIO.cleanup()