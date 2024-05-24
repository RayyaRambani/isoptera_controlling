# import serial
import time
from stepper_control import stepperProgram, cleanup

def menghandleStepper(stepper, cmd):
    if cmd :
        cmd = cmd.lower()
        if cmd in ['a','b','c','d','e','f','g']:
            stepperProgram(stepper, cmd)
        else:
            print(f"invalid cmd buat {stepper}")
            
def mulaiControl():
    try:
        while True:
            data = input("Masukian Perintah : ... : ... : ...")
            parts = data.split()
            if len(parts)==3:
                menghandleStepper('stepper1', parts[0])
                menghandleStepper('stepper1', parts[1])
                menghandleStepper('stepper1', parts[2])
            else:
                print("format ga valid coy. contoh = a:b:c ")
        
    except KeyboardInterrupt:
        print("program keluar")
    finally:
        cleanup()
        
        
mulaiControl()























# def startControll():
#     try:
#         while True:
#             #stepA=???,stepB=???
#             data = input("Masukan Titik Stepper Pertama : ( ... : ... : ... )")
#             parts = data.split(':')
#             if len(parts)==4:
#                 #stepper1
#                 direct = parts[0]
#                 if direct.lower() == 'a':
                    
#                     #programAstepper1
                    
#                     pass
#                 elif direct.lower()  == 'b':
#                     #programBstepper1
#                     pass
#                 # elif:(tambahan)
#                 elif direct == '':
#                     pass
#                 else:
#                     print("invalid input program 1,stepper 1")
                    
#                 #stepper2
#                 direct = parts[1]
#                 if direct.lower() == 'c':
#                     #programAstepper1
#                     pass
#                 elif direct.lower()  == 'd':
#                     #programBstepper1
#                     pass
#                 # elif:(tambahan)
#                 elif direct == '':
#                     pass
#                 else:
#                     print("invalid input program 2, stepper 2")
                
#                 #stepper3
#                 direct = parts[2]
#                 if direct.lower() == 'e':
#                     #programAstepper1
#                     pass
#                 elif direct.lower()  == 'f':
#                     #programBstepper1
#                     pass
#                 # elif:(tambahan)
#                 elif direct == '':
#                     pass
#                 else:
#                     print("invalid input program 3, stepper 3")
                    
#                 # try :
#                 #     direct2 = parts[1]
#                 #     direct2 = parts[2]
#                 #     direct2 = parts[3]
                    
#                 # except ValueError:
#                 #     print("invalid ")
#             else:
#                 print("invalid format gerak robot")
                    
#     except KeyboardInterrupt:
#         print("Program keluar")
            