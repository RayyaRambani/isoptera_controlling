import RPi.GPIO as GPIO
import time

# DIR = 0
# STEP = 0

GPIO.setmode(GPIO.BCM)
stepper_pin = {
    'stepper1':{'DIR': 0, 'STEP':0},
    'stepper2':{'DIR': 0, 'STEP':0},
    'stepper3':{'DIR': 0, 'STEP':0}
}

for pin in stepper_pin.values():
    GPIO.setup(pin['DIR'], GPIO.OUT)
    GPIO.setup(pin['STEP'], GPIO.OUT)
    
def moveStepper(pin,step, direct):
    GPIO.output(pin['DIR'], direct)
    for _ in range(step):
        #editterserah
        GPIO.output(pin['STEP'], GPIO.HIGH)
        time.sleep(0.001)

def sendData(stepper, cmd):
    pin = stepper_pin.get(stepper)
    if not pin:
        print(f"invalid stepper : {stepper}")
        return
 
    #edit keterangan sesuai kebutuhan  
    
    #ATURATUR AJA YA VIN
    
    #stepper1  
    if cmd == 'a':
        moveStepper(pin, 100, GPIO.HIGH)
    elif cmd == 'b':
        moveStepper(pin, 100, GPIO.LOW)
    
    #stepper2
    elif cmd == 'c':
        moveStepper(pin, 100, GPIO.HIGH)
    elif cmd == 'd':
        moveStepper(pin, 100, GPIO.HIGH)
    elif cmd == 'e':
        moveStepper(pin, 100, GPIO.HIGH)
    #stepper2 backward
    elif cmd == 'c':
        moveStepper(pin, 100, GPIO.HIGH)
    
    #stepper3
    elif cmd == 'f':
        moveStepper(pin, 100, GPIO.HIGH)
    elif cmd == 'g':
        moveStepper(pin, 100, GPIO.LOW)
        
        
        






    
def stepperProgram(stepper, cmd):
    if stepper in stepper_pin:
        sendData(stepper, cmd)
    else:
        print(f"stepper {stepper} tidak defined.")
        
def cleanup():
    GPIO.cleanup()