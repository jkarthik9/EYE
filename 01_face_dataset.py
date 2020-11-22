#We use this to create datasets using our integrated webcam in our PC
#Take photos under different light conditions for better perfomance
import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

#Using Haarcascade to identify face in the video stream
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one unique numeric face id
face_id = input('\n enter user id end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0  #change this intial count to take more photos of same person e.g. 30 to 60

while(True):

    ret, img = cam.read()
   # img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break#if you change intial count in line 18 to 30 and below elif count>=60 you can take photos of person which will be saved as e.g. user 1.30 to user 1.60
    elif count >= 30: # Take 30 face samples of a person and stop video
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()


