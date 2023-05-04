import serial
arduinoData=serial.Serial('com3',115200)


while True:

    cmd=input('Please Enter Your Command: ')
    cmd=cmd + '\r'
    arduinoData.write(cmd.encode())

    while arduinoData.in_waiting==0:
        pass
    dataPacket=arduinoData.readline()
    dataPacket=str(dataPacket,'utf-8')
    dataPacket=dataPacket.strip('\r\n')
    dataPacket=dataPacket.split(',')
   
