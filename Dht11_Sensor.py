
import time
import serial
from vpython import *
 
arduinoData=serial.Serial('com3',115200)
time.sleep(.5)
digValue=label(text='50',height=20,box=False,pos=vector(0,-2.5,2))
bulb=sphere(radius=1,color=color.red,pos=vector(0,-3,0))
cyl=cylinder(radius=.6,color=color.red,axis=vector(0,1,0),length=6,pos=vector(0,-3,0))
bulbGlass=sphere(radius=1.2,color=color.white,opacity=.25,pos=vector(0,-3,0))
cylGlass=cylinder(radius=.8,color=color.white,axis=vector(0,1,0),opacity=.25,length=6,pos=vector(0,-3,0))
for temp in range(0,115,10):
    tickPos=4.5/115*temp+1.5
    tick=cylinder(radius=.7,color=color.black,length=.1,axis=vector(0,1,0),pos=vector(0,tickPos-3,0))
    label=text(text=str(temp),color=color.white,pos=vector(-2,tickPos-3,0),height=.3)
while True:
    while arduinoData.in_waiting==0:
        pass
    dataPacket=arduinoData.readline()
    dataPacket=str(dataPacket,'utf-8')
    dataPacket=dataPacket.strip('\r\n')
    dataPacket=dataPacket.split(',')
    temp=float(dataPacket[0])
    hum=float(dataPacket[1])
    len=(4.5/115)*temp+1.5
    cyl.length=len
    digValue.text=str(temp)

