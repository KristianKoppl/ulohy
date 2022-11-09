import tkinter
from random import*
canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()

def pokazeny_semafor():
    canvas.delete('all')
    canvas.after(500,pokazeny_semafor)
    farba= randrange(0,4)
    print(farba)
    canvas.create_rectangle(250,100,300,250,fill='black')
    if farba == 0:
        canvas.create_oval(250,100,300,150,fill='red')
        canvas.create_oval(250,150,300,200,fill='yellow')
    
    if farba == 1:
        
        canvas.create_oval(250,200,300,250,fill='green')
    
    if farba == 2:
        canvas.create_oval(250,100,300,150,fill='red')
        canvas.create_oval(250,150,300,200,fill='yellow')
        canvas.create_oval(250,200,300,250,fill='green')
    
    if farba == 3:    
        canvas.create_oval(250,150,300,200,fill='yellow')

    if farba == 4:
        canvas.create_oval(250,100,300,150,fill='red')
    
pokazeny_semafor()
