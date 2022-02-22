
import cv2
import os
import face_recognition as faceRecognition
import numpy as np
from datetime import datetime

path = 'photo'
images = []
imageLables = []

mylist = os.listdir(path)

for cl in mylist:
    currentImage = cv2.imread(path+ '\\' + cl)
    images.append(currentImage)
    imageLables.append(os.path.splitext(cl)[0])


def findEncodings(images):
    encodList=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=faceRecognition.face_encodings(img)[0]
        encodList.append(encode)
    return encodList

encodlstKnowFaces=findEncodings(images)

webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
nm = 'a'

while True:
    success,capturedImage =webcam.read()
    imageResize = cv2.resize(capturedImage,(0,0),None,0.25,0.25)
    imageResize = cv2.cvtColor(capturedImage,cv2.COLOR_BGR2RGB)

    faceCurrentFrame = faceRecognition.face_locations(imageResize)
    encodeCurrentFrame = faceRecognition.face_encodings(imageResize,faceCurrentFrame)

    for encodeFace, faceLocation in zip(encodeCurrentFrame,faceCurrentFrame):
        matches = faceRecognition.compare_faces(encodlstKnowFaces,encodeFace)
        faceDistance = faceRecognition.face_distance(encodlstKnowFaces,encodeFace)

        matchesIndex = np.argmin(faceDistance)

        if(matches[matchesIndex]):
            name = imageLables[matchesIndex].upper()
            y1,x2,y2,x1 = faceLocation
            # y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            
            cv2.rectangle(capturedImage,(x1,y1),(x2,y2),(0,255,0),3)  
            # cv2.rectangle(capturedImage,(x1,y1-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(capturedImage,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            currentTime = datetime.now().time()
            currentDate = datetime.now().date()

            if name!=nm:
                print(name +'  '+str(currentDate)+' '+str(currentTime))
                nm=name
            
    cv2.imshow('Frame',capturedImage)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

webcam.release()
cv2.destroyAllWindows()
