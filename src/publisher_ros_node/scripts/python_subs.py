#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import serial
import time
i = 1
current_b = 90
current_n = 90

ser = serial.Serial("/dev/ttyACM0", 115200)

def fun_initiater():
    ser.write('a90:90\n')
    global current_b
    global current_n
    current_b = 90
    current_n = 90
    print("=============================================================")

def fun_call(msg):
    rospy.loginfo(msg)
    global current_b
    global current_n
    print(str(current_b))
    print(str(current_n))

    txt = str(msg.data)

    b = int(txt.split(":", 1)[0])
    n = int(txt.split(":", 1)[1])
    #if b!=0 or n!=0:
    if abs(b)>1 or abs(n)>1:
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
        print(str(command))

    
    

if __name__ == '__main__':
    rospy.init_node('nodepythonarduino')
    if i==i:
        fun_initiater()
        i = 2
    sub = rospy.Subscriber("/face_angle_topic",String, fun_call)
    
    rospy.spin()
