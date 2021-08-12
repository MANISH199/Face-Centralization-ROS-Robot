#!/usr/bin/env python

from std_msgs.msg import String
import serial
from serial import Serial
import time

ser = serial.Serial("/dev/ttyACM0", 115200)


i = 1
current_b = 90
current_n = 90



def fun_initiater():
    print("=============================================================")
    ser.write(b'a90:90\n')
    global current_b
    global current_n
    current_b = 90
    current_n = 90
    print("=============================================================")

def fun_call(strr):
    b = 0
    n = 0
    global current_b
    global current_n
    if strr == "a":
        b = 10
        n = 10
    elif strr == "b":
        b = -10
        n = -10
    elif strr == "c":
        ser.write(b'a101:86\n')
        current_b = 90
        current_n = 90
    elif strr == "d":
        ser.write(b'a90:90\n')
        current_b = 90
        current_n = 90


    if b != 0 and n!=0:
        
        print(str(current_b))
        print(str(current_n))
        current_b = int (current_b) - b
        current_n = int(current_n) + n
        if current_b > 180:
            current_b = 180
        elif current_b < 0:
            current_b = 0
        if current_n > 180:
            current_n = 180
        elif current_n < 0:
            current_n = 0
        command = "a"+str(current_b)+":"+str(current_n)+"\n"
        ser.write(command.encode())
    
        #time.sleep(1)
        print(str(command.encode()))

    
    

if __name__ == '__main__':
    fun_initiater()
    while (1):
        inval = input("enter a or b")
        print ("entry : " + inval)
        fun_call(inval)
        
    
