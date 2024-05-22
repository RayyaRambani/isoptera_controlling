# import RPi.GPIO as GPIO
# import time

# #motor1
# in1 = 17
# in2 = 18
# ena = 22

# #motor2
# in3 = 17
# in4 = 18
# enb = 22


# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(in1, GPIO.OUT)
# GPIO.setup(in2, GPIO.OUT)
# GPIO.setup(ena, GPIO.OUT)
# GPIO.setup(in3, GPIO.OUT)
# GPIO.setup(in4, GPIO.OUT)
# GPIO.setup(enb, GPIO.OUT)

# pwmA = GPIO.PWM(ena, 100)
# pwmA.start(0)
# pwmB = GPIO.PWM(enb, 100)
# pwmB.start(0)

# def forwardMA():
#     GPIO.output(in1, GPIO.HIGH)
#     GPIO.output(in2, GPIO.LOW)
# def backwardMA():
#     GPIO.output(in1, GPIO.LOW)
#     GPIO.output(in2, GPIO.HIGH)
# def forwardMB():
#     GPIO.output(in3, GPIO.HIGH)
#     GPIO.output(in4, GPIO.LOW)
# def backwardMB():
#     GPIO.output(in3, GPIO.LOW)
#     GPIO.output(in4, GPIO.HIGH)
# def stop():
#     GPIO.output(in1, GPIO.LOW)
#     GPIO.output(in2, GPIO.LOW)
#     GPIO.output(in3, GPIO.LOW)
#     GPIO.output(in4, GPIO.LOW)
    
    
# def set_motor(speed, direct):
#     if direct =='maju' or direct=='Maju':
#         forwardMA()
#         forwardMB()
#         pwmA.ChangeDutyCycle(80)
#         pwmB.ChangeDutyCycle(80)
#         time.sleep(2)
        
#     elif direct =='mundur' or 'Mundur':
#         backwardMA()
#         backwardMB()
#         pwmA.ChangeDutyCycle(80)
#         pwmB.ChangeDutyCycle(80)
#         time.sleep(2)
        
#     elif direct =='Kiri' or direct=='kiri' :
#         backwardMA()
#         forwardMB()
#         pwmA.ChangeDutyCycle(80)
#         pwmB.ChangeDutyCycle(80)
#         time.sleep(2)
#     elif direct =='kanan' or 'Kanan':
#         forwardMA()
#         backwardMB()
#         pwmA.ChangeDutyCycle(80)
#         pwmB.ChangeDutyCycle(80)
#         time.sleep(2)
#     else:
#         stop()
#         pwmA.ChangeDutyCycle(0)
#         pwmB.ChangeDutyCycle(0)
#         time.sleep(2)
    
    