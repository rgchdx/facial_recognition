import cv2
import face_recognition
import face_recognition_models
import pickle
import os

# Importing the face images
folderPath = 'Images'
pathList = os.listdir(folderPath)  # obtain all of the files in the folder and put it in a list
imgList = []  # create empty list to store all the images
faceIds = []  # create empty list to store all the face ids
for path in pathList:  # iterate through the list of files
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    faceIds.append(os.path.splitext(path)[0])  # we use cv2 to read the images and append it to the list. Use os.path.join to get the full path of the image
    #Splitting to get the id and png part separated. The 0 will only extract the id since it will be the first part
print(len(imgList))