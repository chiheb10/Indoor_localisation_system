import serial
import time
import io
import json
import re
import socket
ser=serial.Serial('COM15',115200,timeout=0.001)
ser.write(b'\x0D')
ser.flush()
ser.write(b'\x0D')
ser.flush()
ser.write(b'les')
ser.flush()
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(("127.0.0.1", 8080))
serv.listen(5)
while(1):
        try:
                conn, addr = serv.accept()
        except(e):
                print("not aleardy connected")
        while(1):
                v=ser.readlines()
                if(len(v)!=0):
                        for line in v:
                                c=str(line)
                                if(line[0]==32)and (len(c)>20):
                                        y=c[11:20].split(',')
                                        x=int(100*float(y[0]))
                                        y=int(100*float(y[1]))
                                        s=str(x)+" "+str(y)+"\n"
                                        conn.send(bytes(s,encoding='utf-8', errors='strict'))
                                

        

                


