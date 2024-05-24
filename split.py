
while True:
    data = input("masukan text : ")
    parts = data.split(':')
    if len(parts)==2:
        direct = parts[0]
        if direct.lower() == 'a':
            # programAstepper1
            pass  # placeholder for the actual code
        elif direct.lower() == 'b':
            # programBstepper1
            pass  # placeholder for the actual code
        elif direct == '':
            pass
        else:
            print("Invalid input for program stepper 1")
        
        
        direct2 = parts[1]
        if direct2.lower() == 'c':
            # programAstepper1
            pass  # placeholder for the actual code
        elif direct2.lower() == 'd':
            # programBstepper1
            pass  # placeholder for the actual code
        elif direct2 == '':
                    pass
        else:
            print("Invalid input for program stepper 1")
        # try :
        #     direct2 = parts[1]
        # except ValueError:
        #     print("invalid nilai kecepatan")
    else:
        print("invalid format gerak robot")
    
    print(f'data 1 = {direct}')
    print(f'data 2 = {direct2}')
    # print("data 3 = {parts[2]}")
    