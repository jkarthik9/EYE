#Our model is just a prototype it will not be 100% accurate in detecting faces 
import cv2
import numpy as np
import os 
import time
import threading
from twilio.rest import Client
#defining function for sms
def threadsms():
	#We used twilio to send sms alert to mobile
            account_sid = ''
            auth_token = ''
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                     body="Accused found at camera-1" ,
                     from_='',
                     to=''
                 )
#To print output on the screen
            print(message.sid)
            print(str(id))
            print("found at camera--1")
            for ctr in range(1,1000) :
                print()


#th = threading.Thread(target=threadsms)
#using HaarCasacade
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> personx: id=1,  etc
names = ['None', 'suspect1', 'suspect2', 'suspect3', 'suspect4', 'suspect5'] 

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:

    ret, img =cam.read()
   # img = cv2.flip(img, -1) # Flip vertically

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2, 
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 46):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            #th.start()
            #threading.Thread(target=threadsms).start()
            #th.join()
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img,names[5], (x+5,y-5), font, 1, (255,255,255), 2)
       #cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera1',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
