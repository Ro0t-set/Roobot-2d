import serial
import time
import sys


ser = serial.Serial ('/dev/ttyACM0',)
ser.baudrate = 115200
ser.close()
print ('Using SerialPort:')
print (ser.name)
ser.open()
print(ser.readline())
ser.write(str('Start').encode())
read0  = float(ser.readline().strip())
read1  = float(ser.readline().strip())
read2  = float(ser.readline().strip())
read3  = float(ser.readline().strip())
read4  = float(ser.readline().strip())
read5  = float(ser.readline().strip())
read6  = float(ser.readline().strip())
read7  = float(ser.readline().strip())
read8  = float(ser.readline().strip())
read9  = float(ser.readline().strip())
read10 = float(ser.readline().strip())
read11 = float(ser.readline().strip())
read12 = float(ser.readline().strip())
read13 = float(ser.readline().strip())
read14 = float(ser.readline().strip())
read15 = float(ser.readline().strip())
read16 = float(ser.readline().strip())
read17 = float(ser.readline().strip())
read18 = float(ser.readline().strip())
read19 = float(ser.readline().strip())
read20 = float(ser.readline().strip())
read21 = float(ser.readline().strip())
read22 = float(ser.readline().strip())
read23 = float(ser.readline().strip())
read24 = float(ser.readline().strip())
read25 = float(ser.readline().strip())
read26 = float(ser.readline().strip())
read27 = float(ser.readline().strip())
read28 = float(ser.readline().strip())
read29 = float(ser.readline().strip())
read30 = float(ser.readline().strip())
read31 = float(ser.readline().strip())
read32 = float(ser.readline().strip())
read33 = float(ser.readline().strip())
read34 = float(ser.readline().strip())
read35 = float(ser.readline().strip())
read36 = float(ser.readline().strip())
read37 = float(ser.readline().strip())
read38 = float(ser.readline().strip())
read39 = float(ser.readline().strip())
read40 = float(ser.readline().strip())
read41 = float(ser.readline().strip())
read42 = float(ser.readline().strip())
read43 = float(ser.readline().strip())
read44 = float(ser.readline().strip())
read45 = float(ser.readline().strip())
read46 = float(ser.readline().strip())
read47 = float(ser.readline().strip())
read48 = float(ser.readline().strip())
read49 = float(ser.readline().strip())
read50 = float(ser.readline().strip())
read51 = float(ser.readline().strip())
read52 = float(ser.readline().strip())
read53 = float(ser.readline().strip())
read54 = float(ser.readline().strip())
read55 = float(ser.readline().strip())
read56 = float(ser.readline().strip())
read57 = float(ser.readline().strip())
read58 = float(ser.readline().strip())
read59 = float(ser.readline().strip())
read60 = float(ser.readline().strip())
read61 = float(ser.readline().strip())
read62 = float(ser.readline().strip())
read63 = float(ser.readline().strip())
read64 = float(ser.readline().strip())
read65 = float(ser.readline().strip())
read66 = float(ser.readline().strip())
read67 = float(ser.readline().strip())
read68 = float(ser.readline().strip())
read69 = float(ser.readline().strip())
read70 = float(ser.readline().strip())
read71 = float(ser.readline().strip())
ser.close()
print (read0)
print (read1)
# print (read2)
# print (read3)
# print (read4)
# print (read5)
# print (read6)
# print (read7)
# print (read8)
# print (read9)
# print (read10)
# print (read11)
# print (read12)
# print (read13)
# print (read14)
# print (read15)
# print (read16)
# print (read17)
# print (read18)
# print (read19)
# print (read20)
# print (read21)
# print (read22)
# print (read23)
# print (read24)
# print (read25)
# print (read26)
# print (read27)
# print (read28)
# print (read29)
# print (read30)
# print (read31)
# print (read32)
# print (read33)
# print (read34)
# print (read35)
print (read36)
print (read37)
# print (read38)
# print (read39)
# print (read40)
# print (read41)
# print (read42)
# print (read43)
# print (read44)
# print (read45)
# print (read46)
# print (read47)
# print (read48)
# print (read49)
# print (read50)
# print (read51)
# print (read52)
# print (read53)
# print (read54)
# print (read55)
# print (read56)
# print (read57)
# print (read58)
# print (read59)
# print (read60)
# print (read61)
# print (read62)
# print (read63)
# print (read64)
# print (read65)
# print (read66)
# print (read67)
# print (read68)
# print (read69)
# print (read70)
# print (read71)
print ("Mapping ended!")

if __name__ == '__main__':
    sys.exit(main())
