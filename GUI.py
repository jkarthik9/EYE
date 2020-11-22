#GUI for our project is done using Tkinter
#please download the bg picutre and place the path in line 34
#import tkinter
from tkinter import *
import os
from PIL import ImageTk,Image

root=Tk()
def function1():
    
    os.system("01_face_dataset.py")

    
def function2():
    
    os.system("02_face_training.py")

def function3():
    
    os.system("03_face_recognition.py")

def function4():

    root.destroy()

#set width and height

canvas=Canvas(root,width=1440,height=1010)

#give this image path. image should be in png format.

#Example: "C:\\Users\\DELL\\OneDrive\\Pictures\\image.png"

image=ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Desktop\\BGorg.png"))

canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
btn=Button(root, text="ENTER DATA",font=('times new roman',20),bg='white', fg='black',command=function1)
btn.place(x=660, y=300)
btn=Button(root, text="TRAIN FACES",font=('times new roman',20),bg='white', fg='black',command=function2)
btn.place(x=660, y=380)
btn=Button(root, text="RUN SURVEILLANCE",font=('times new roman',20),bg='white', fg='black',command=function3)
btn.place(x=620, y=460)
btn=Button(root, text="EXIT",font=('times new roman',20),bg='white', fg='black',command=function4)
btn.place(x=710, y=540)
root.mainloop()
