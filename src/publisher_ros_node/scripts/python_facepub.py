#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import serial
import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')
# beter give direct path, since it's an issue with melodic
#face_cascade = cv2.CascadeClassifier('/home/manish/DATA/WORKSHOPE/Python/FaceDetection/haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('/home/manish/DATA/WORKSHOPE/Python/FaceDetection/haarcascade_eye.xml')
# index should be given manualy , mostly 0 for built in webcam
cap = cv2.VideoCapture(2)

if __name__ == '__main__':
    rospy.init_node('nodepythonfacedet')

    pub = rospy.Publisher("/face_node_topic", String, queue_size=10)
    rate = rospy.Rate(10)
    Subr = 0
    while not rospy.is_shutdown():
        ret, img = cap.read()
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        fx = int(img.shape[1] / 2)
        fy = int(img.shape[0] / 2)
        fa = 0
        fap = 0
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            fa = int(w * h)
            if fa > fap:
                fap = fa
                fx = int(x + w / 2)
                fy = int(y + h / 2)

        img = cv2.circle(
            img, (int(img.shape[1] / 2), int(img.shape[0] / 2)), 5, (0, 100, 0), 2)
        img = cv2.line(img, (fx, fy), (int(
            img.shape[1] / 2), int(img.shape[0] / 2)), (230, 90, 50), 2)
        cv2.imshow('img', img)
        moveval = "x=" + \
            str(int(img.shape[1] / 2) - fx) + ":y=" + \
            str(int(img.shape[0] / 2) - fy)
        k = cv2.waitKey(30) & 0xff
        #print (k)
        if k == 27:
            break
        msg = String()
        msg.data = moveval
        # to reduce the count of publish
        if Subr == 10:
            pub.publish(msg)
            Subr = 0
        else:
            Subr = Subr + 1
        rate.sleep()
    cap.release()
    cv2.destroyAllWindows()

    rospy.loginfo("nodepythonfacedet is down")
