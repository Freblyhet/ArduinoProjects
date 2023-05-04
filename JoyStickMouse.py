import serial
import pydirectinput
from pynput.mouse import Button, Controller
mouse = Controller()

arduino = serial.Serial('COM3', 115200, timeout=.1)     #serial input from arduino. change COM port to wherever your arduino is connected

pydirectinput.PAUSE = 0

keysDown = {}   #list of currently pressed keys


def keyDown(key):               #what to do if key pressed. takes value from handleJoyStickAsArrowKeys
    keysDown[key] = True        #adds key to KeysDown list
    pydirectinput.keyDown(key)  #runs pydirectinput using key from (argument)
    print('Down: ', key)       #remove '#' from print to test data stream


def keyUp(key):                     #what to do if key released. takes value from handleJoyStickAsArrowKeys
    if key in keysDown:
        del (keysDown[key])         #remove key from KeysDown
        pydirectinput.keyUp(key)    #runs pydirectinput using key from (argument)
        print('Up: ', key)         #remove '#' from print to test data stream


#def handleJoyStickAsArrowKeys(x, y, z, f):      #note that the x and y directions are swapped due to the way I orient my thumbstick


def handleJoyStickAsArrowKeys(x,y,z,f):
    if x == 0:          #0 is up on joystick
        keyDown('down')   #add up key to keyDown (argument)
        keyUp('up')   #add down key to keyUp (argument), as you can't press up and down together
    elif x == 2:        #2 is down on joystick
        keyDown('up')
        keyUp('down')
    else:               #1 is neutral on joystick
        keyUp('up')
        keyUp('down')

    if y == 2:          #2 is right on joystick
        keyDown('right')
        keyUp('left')
    elif y == 0:        #0 is left on joystick
        keyDown('left')
        keyUp('right')
    else:               #1 is neutral on joystick
        keyUp('left')
        keyUp('right')
    if z == 1:          #z argument is JSButton in this case. 1 is button pressed
        keyDown('space')   #key to be pressed with Joystick button. Change to any key
    else:
        keyUp('space')
    if f == 1:          #z argument is JSButton in this case. 1 is button pressed
        keyDown('enter')   #key to be pressed with Joystick button. Change to any key
    else:
        keyUp('enter')



while True:
    rawdata = arduino.readline()            #read serial data from arduino one line at a time
    data = str(rawdata.decode('utf-8'))     #decode the raw byte data into UTF-8
    if data.startswith("S"):                #make sure the read starts in the correct place
        dx = int(data[1])                   #X direction is second digit in data (data[0] is 'S')
        dy = int(data[3])                   #Y direction is fourth digit in data
        z = int(data[5])
        f = int(data[7])
        #dX = int(data[9])                   #X direction is second digit in data (data[0] is 'S')
        #dY = int(data[11]) 
                 
        #print(dx, dy, JSButton)            #remove '#' from print to test data stream
        handleJoyStickAsArrowKeys(dx, dy, z, f) 
        #handleJoyStickAsMouse(dx, dy, z, f)