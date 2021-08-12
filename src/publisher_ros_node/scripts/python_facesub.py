#!/usr/bin/env python

import rospy
import math
import time
from std_msgs.msg import String
Gn = 1234
Gb = 1646
angleval ="0:0"

def fun_call(msg):
    rospy.loginfo(msg)
    txt = str(msg.data)
    x = txt.split(":", 1)[0]
    xp = x.split("=", 1)[1]
    y = txt.split(":", 1)[1]
    yp = y.split("=", 1)[1]

    xa_b = int(round(math.degrees(math.atan(float(xp)/float(Gb)))))
    ya_n = int(round(math.degrees(math.atan(float(yp)/float(Gn)))))
    #xa_n = str(math.degrees(math.atan(0.0405)))
    angleval = str(xa_b)+":"+ str(ya_n)
    print(angleval)
    print(str(xa_b))
    print(str(ya_n))

    pub = rospy.Publisher("/face_angle_topic", String, queue_size = 10)
    msg = String()
    msg.data = angleval
    pub.publish(msg)
    #time.sleep(1)


if __name__ == '__main__':
    rospy.init_node('nodepythonfacedetsub')

    sub = rospy.Subscriber("/face_node_topic",String, fun_call)
    
    rospy.spin()