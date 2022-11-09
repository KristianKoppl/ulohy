import tkinter
from random import *

canvas = tkinter.Canvas(width=600,height=500)
canvas.pack()




def bomba():
    time = 60


    time-=1
    if time >=60:
        time-=1
    canvas.update()
    canvas.after(1000,bomba)
    print(time)
                                        
def daco():
    bomba()

daco()








entry1=tkinter.Entry()
entry1.pack()
