
import cv2.cv2 as cv2
#import os

############################################################################################
frameWidth = 640
frameHeight = 480
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
############################################################################################

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 80)

while True:
    success, img = cap.read(1)                                      #Get the Webcamimage

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                 #Convert it from BRG to Greycolor scale

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4 ,)         #use FaceCasadefuntion
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        print("face detected:")                                     #Theoreticly not neccessery



   # def labels_for_training_data(directory):
    #    faces=[]
     #   faceID=[]

      #  for path, subdirnames, filenames in os.walk(directory):
       #     for filename in filenames:
        #        if filename.startswith("."):
         #           print("Skipping system file"
          #          continue

    cv2.imshow("video", img)                                        #Show us the Webcamimage

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
