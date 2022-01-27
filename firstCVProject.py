from tkinter import *
import numpy
import cv2

def startSaving():
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('video.avi' , fourcc , 20.0 , (640,480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            out.write(frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

top = Tk()

top.geometry('500x250')

b = Button(top , text='Start Recording' , command=startSaving , activeforeground='white' , activebackground='black' , pady=10)

b.pack(side=LEFT)

top.mainloop()