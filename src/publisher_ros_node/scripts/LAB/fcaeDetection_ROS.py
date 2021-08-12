import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')
#face_cascade = cv2.CascadeClassifier('/home/manish/DATA/WORKSHOPE/Python/FaceDetection/haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('/home/manish/DATA/WORKSHOPE/Python/FaceDetection/haarcascade_eye.xml')
cap = cv2.VideoCapture(2)
while 1:
    ret, img = cap.read()
    img = cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    fx = int(img.shape[1]/2)
    fy = int(img.shape[0]/2)
    fa = 0
    fap = 0

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        fa = int(w*h)
        if fa>fap:
            fap = fa
            fx = int(x+w/2)
            fy = int(y+h/2)

        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    img = cv2.circle(img, (int(img.shape[1]/2),int(img.shape[0]/2)), 5, (0,100,0), 2)
    img = cv2.line(img, (fx,fy), (int(img.shape[1]/2),int(img.shape[0]/2)), (230,90,50), 2)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff

    xm = int(img.shape[1]/2) - fx
    ym = int(img.shape[0]/2) - fy
    moveval =  "x=" +str(int(img.shape[1]/2) - fx)+":y="+str(int(img.shape[0]/2) - fy)

    dimens =  "x=" +str(int(img.shape[1]))+":y="+str(int(img.shape[0]))
    print (dimens)

    print (moveval)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
