import tkinter
import random

canvas = tkinter.Canvas(width=600,height=500)
canvas.pack()
 

def kvapka():
    global x,y
    global x1,y1
    global x2,y2
    
    pocet_kvapiek=0
    dosiahne = 0
    nieco = 0
    x1 = 255
    x2 = 335
    y1 = 480
    y2 = 465
    canvas.delete('all')

    canvas.create_oval(x-15,y-15,x+15,y+15,fill='blue')
    canvas.create_oval(50,450,530,490)
    canvas.create_oval(50,440,530,420)
    canvas.create_line(50,470,50,430)
    canvas.create_line(530,470,530,430)
    
    y += 5
    x1 += 5
    x2 += 5
    y1 += 5
    y2 += 5
    print(y)

    if y >= 470:
        pocet_kvapiek+=1
        print(pocet_kvapiek)
        nieco += 1
        canvas.create_oval(x1+5,y1+5,x2+5,y2+5,fill='blue')
        
    if y >= 470:
        y = 50
    if go == 1:
        canvas.after(100,kvapka)

    

    

    
        
           
go = 1
x = 300
y = 50

kvapka()
