import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade= cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)  
flag=True
count=0
while flag:
    flag, img = cap.read()  #2 return , flag and frame
    gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gr,1.1,4)
    eyes = eyes_cascade.detectMultiScale(gr,1.1,4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (200, 200, 200), 2)
    print(eyes)
    for (x,y,w,h) in eyes:
        cv2.circle(img,(int(0.92*x+0.95*w),int(0.9*y+0.9*h)),h//2,(255,0,0),2)
        
    if count<30:
        if len(eyes)==0:count+=1
        else:count=0
    else:
        print("Open eyes not detected for 3 sec,stopping vehicle")  # apply breaks or stop vehicle or play beeps
        break
        
    
    cv2.imshow('img', img)

    w=cv2.waitKey(1)# & 0xff # biwise and with 255


cap.release()