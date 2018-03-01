import serial
import time

#'/dev/x': la x va campiata in base al proprio dispositivo e verificando la po

ser = serial.Serial ('/dev/cu.usbmodem14321',)
ser.baudrate = 115200
ser.close()

print ('Using SerialPort:') 
print (ser.name)
ser.open()


#i dati dai sensori si alternano: i pari vanno sono Sensore1 e i dispari Sensore2

read0 = int(ser.readline())
read1 = int(ser.readline())
read2 = int(ser.readline())
read3 = int(ser.readline())
read4 = int(ser.readline())
read5 = int(ser.readline())
read6 = int(ser.readline())
read7 = int(ser.readline())
read8 = int(ser.readline())
read9 = int(ser.readline())
read10 = int(ser.readline())
read11 = int(ser.readline())
read12 = int(ser.readline())
read13 = int(ser.readline())
read14 = int(ser.readline())
read15 = int(ser.readline())
read16 = int(ser.readline())
read17 = int(ser.readline())
read18 = int(ser.readline())
read19 = int(ser.readline())
read20 = int(ser.readline())
read21 = int(ser.readline())
read22 = int(ser.readline())
read23 = int(ser.readline())
read24 = int(ser.readline())
read25 = int(ser.readline())
read26 = int(ser.readline())
read27 = int(ser.readline())
read28 = int(ser.readline())
read29 = int(ser.readline())
read30 = int(ser.readline())
read31 = int(ser.readline())
read32 = int(ser.readline())
read33 = int(ser.readline())
read34 = int(ser.readline())
read35 = int(ser.readline())






ser.close()


print (read0)

print (read1)

print (read2)

print (read3)

print (read4)

print (read5)

print (read6)

print (read7)

print (read8)

print (read9)

print (read10)

print (read11)

print (read12)

print (read13)

print (read14)

print (read15)

print (read16)

print (read17)

print (read18)

print (read19)
print (read20)
print (read21)

print (read22)
print (read23)

print (read24)
print (read25)

print (read26)

print (read27)

print (read28)

print (read29)

print (read30)

print (read31)

print (read32)
print (read33)
print (read34)
print (read35)
print ("Mapping ended!")


