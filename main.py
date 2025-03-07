import cv2

###Webcam setup###
cap = cv2.VideoCapture(0) #if using multiple cameras, have 1 instead of 0
cap.set(3,1280,) #set width of the frame
cap.set(4,720) #set height of the frame

while True:
    successs, img = cap.read()
    cv2.imshow("Face Attendance",img)
    cv2.waitKey(1)