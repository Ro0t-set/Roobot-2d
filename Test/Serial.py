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

read0 = ser.readline()
read1 = ser.readline()
read2 = ser.readline()
read3 = ser.readline()
read4 = ser.readline()
read5 = ser.readline()
read6 = ser.readline()
read7 = ser.readline()
read8 = ser.readline()
read9 = ser.readline()
read10 = ser.readline()
read11 = ser.readline()
read12 = ser.readline()
read13 = ser.readline()
read14 = ser.readline()
read15 = ser.readline()
read16 = ser.readline()
read17 = ser.readline()
read18 = ser.readline()
read19 = ser.readline()
read20 = ser.readline()
read21 = ser.readline()
read22 = ser.readline()
read23 = ser.readline()
read24 = ser.readline()
read25 = ser.readline()
read26 = ser.readline()
read27 = ser.readline()
read28 = ser.readline()
read29 = ser.readline()
read30 = ser.readline()
read31 = ser.readline()
read32 = ser.readline()
read33 = ser.readline()
read34 = ser.readline()
read35 = ser.readline()






ser.close()

# print (read0)
# print (read1)
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
print ("Mapping ended!")

