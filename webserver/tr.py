import serial
import time
import io
import json
import re
import socket
ser=serial.Serial('COM14',115200,timeout=1)
ser.write(b'\x0D')
ser.flush()
ser.write(b'\x0D')
ser.flush()
ser.write(b'apg')
ser.flush()

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(("192.168.137.1", 8080))
serv.listen(5)
while(1):
        try:
                conn, addr = serv.accept()
        except(e):
                print("not aleardy connected")
        while(1):
                ser.write(b'\x0D')
                time.sleep(0.01)
                for line in ser.readlines():
                        if(line[0]==120):
                                r=str(line)[2:-5]
                                v=re.split(':| ',r)
                                s=v[1]+" "+v[3]
                                print(s)
                                conn.send(bytes(s,encoding='utf-8', errors='strict'))
     


