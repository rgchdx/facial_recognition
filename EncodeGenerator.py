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
print(faceIds)

def findEncoding(imgList):
    encodeList = []  # create empty list to store all the encodings
    for image in imgList:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # convert the image from BGR to RGB since cv uses BGR by default
        encode = face_recognition.face_encodings(img)[0] # find the face encodings of the image
        encodeList.append(encode)
    return encodeList

print('Encoding Started')
encodeListKnown = findEncoding(imgList)
encodeListKnownWithIds = [encodeListKnown, faceIds]
print('Encoding Complete')

file = open('EncodeFile.p', 'wb')  # open a file in write binary mode
pickle.dump(encodeListKnownWithIds, file)  # dump the encodeListKnownWithIds to the file
file.close()
print('Encode File Saved')
        