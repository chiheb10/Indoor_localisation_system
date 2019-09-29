import serial
import time
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM14'
ser.open()
ser.write(b'\0x0D')
time.sleep(1)
ser.write(b'\0x0D')
ser.write(b'apg')
v=ser.read(10)


