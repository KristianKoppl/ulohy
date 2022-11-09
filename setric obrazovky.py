import tkinter
from random import*
canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()




def setric():
    uhol = 0
    color=choice(('red','green','blue','white','orange','yellow','black','lime','purple','pink'))
    canvas.delete('all')
    canvas.after(1000,setric)
    canvas.create_text(randrange(0,490),randrange(0,490),text= entry1.get(),font='Arial 30',fill=color,angle = uhol)
    if uhol >=90:
        uhol = 0
    else:
        uhol += 10
    
    
def zmaz(event):
    canvas.delete('all')







entry1 = tkinter.Entry()
entry1.pack()
setric()

canvas.bind('<Button-1>', zmaz)
