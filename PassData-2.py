import serial
from vpython import *

arduinoData=serial.Serial('com3',115200)

myOrb=sphere(color=color.black,radius=1)

while True:
    myCmd=input('Please Input Your Color R:G:B 0-255 ')
    myCmd=myCmd+'\r'
    arduinoData.write(myCmd.encode())
    myColor=myCmd.split(':')
    red=int(myColor[0])
    green=int(myColor[1])
    blue=int(myColor[2])
    myOrb.color=vector(red/255,green/255,blue/255)