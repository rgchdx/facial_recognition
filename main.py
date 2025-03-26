import os
import cv2

### Webcam setup ###
cap = cv2.VideoCapture(0)  # If using multiple cameras, change 0 to 1
cap.set(3, 680)  # Set width slightly smaller than 720
cap.set(4, 510)  # Set height slightly smaller than 540

imgBackground = cv2.imread("Resources/background.png")

###Importing the mode images into a list###
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath) #obtain all of the files in the folder and put it in a list
imgModeList = [] #create empty list to store all the images
for path in modePathList: #iterate through the list of files
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path))) #we use cv2 to read the images and appepend it to the list. Use os.path.join to get the full path of the image
#print(len(imgModeList))

### What the webcam will show ###
while True:
    success, img = cap.read()
    
    # Resize the webcam feed to match the new dimensions
    img_resized = cv2.resize(img, (680, 510))  
    mode_img_height, mode_img_width = imgModeList[0].shape[:2]
    mode_img_resized = cv2.resize(imgModeList[0], (470, 700))
    
    
    # Place the resized webcam feed in the background
    imgBackground[175:175+510, 60:60+680] = img_resized  # Adjusted placement
    imgBackground[50:50+700, 855:855+470] = mode_img_resized

    cv2.imshow("Webcam", img_resized)
    cv2.imshow("Face Attendance", imgBackground)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()