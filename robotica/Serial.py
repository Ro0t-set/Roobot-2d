import serial
import time



ser = serial.Serial ('/dev/ttyACM0',)
ser.baudrate = 115200
ser.close()

print ('Using SerialPort:') 
print (ser.name)
ser.open()
read = ser.readline()

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

ser.close()

print (read)

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







