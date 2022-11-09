import tkinter
import random

canvas = tkinter.Canvas(width=600,height=550)
canvas.pack()
 

def bosorky():
    global x,y
    global x1,y1
    global x2,y2

    dosiahne = 0
    nieco = 0
    canvas.delete('all')

    bosorka1 = canvas.create_oval(x-15,y-45,x+15,y-15,fill='white')
    bosorka1 = canvas.create_rectangle(x-15,y-15,x+15,y+45,fill='white')
    bosorka1 = canvas.create_line(x-45,y+25,x+55,y+25,fill='black',)

    bosorka2 = canvas.create_oval(x-200,y-145,x-170,y-115,fill='white')
    bosorka2 = canvas.create_rectangle(x-200,y-115,x-170,y-45,fill='white')
    bosorka2 = canvas.create_line(x-245,y-75,x-105,y-75,fill='black',)
    
    bosorka1 = canvas.create_line(x-85,y+45,x-45,y+25,fill='black',)
    bosorka1 = canvas.create_line(x-85,y+55,x-45,y+25,fill='black',)
    bosorka1 = canvas.create_line(x-85,y+65,x-45,y+25,fill='black',)
    bosorka1 = canvas.create_line(x-85,y+75,x-45,y+25,fill='black',)
    bosorka1 = canvas.create_line(x-85,y+25,x-45,y+25,fill='black',)
    bosorka1 = canvas.create_line(x-85,y+35,x-45,y+25,fill='black',)
    bosorka1 = canvas.create_line(x-85,y+15,x-45,y+25,fill='black',)
    bosorka1 = canvas.create_line(x-85,y+5,x-45,y+25,fill='black',)
    bosorka1 = canvas.create_line(x-85,y+-5,x-45,y+25,fill='black',)
    bosorka1 = canvas.create_line(x-85,y-15,x-45,y+25,fill='black',)

    bosorka2 = canvas.create_line(x-285,y-105,x-245,y-75,fill='black',)
    bosorka2 = canvas.create_line(x-285,y-95,x-245,y-75,fill='black',)
    bosorka2 = canvas.create_line(x-285,y-85,x-245,y-75,fill='black',)
    bosorka2 = canvas.create_line(x-285,y-75,x-245,y-75,fill='black',)
    bosorka2 = canvas.create_line(x-285,y-65,x-245,y-75,fill='black',)
    bosorka2 = canvas.create_line(x-285,y-55,x-245,y-75,fill='black',)
    bosorka2 = canvas.create_line(x-285,y-45,x-245,y-75,fill='black',)
    bosorka2 = canvas.create_line(x-285,y-35,x-245,y-75,fill='black',)
    bosorka2 = canvas.create_line(x-285,y-25,x-245,y-75,fill='black',)
    bosorka2 = canvas.create_line(x-285,y-15,x-245,y-75,fill='black',)

    canvas.create_rectangle(0,520,610,560,fill='saddle brown',outline='green',width=4)
    
    y += 5
    x1 += 5
    x2 += 5
    y1 += 5
    y2 += 5

    if y > 470:
        nieco += 1
    if y > 470:
        y = 470
        
    if go == 1:
        canvas.after(random.randrange(-1,11),bosorky)

    if nieco == 1:
        canvas.create_oval(x1+5,y1+5,x2+5,y2+5,fill='blue')
        nieco = 1

    if y > 470:
        dosiahne += 1

    if  dosiahne == 470:
        canvas.create_oval(x1+5,y1+5,x2+5,y2+5,fill='blue')
        dosiahne = 1

   

def zem():
    canvas.create_rectangle(0,450,600,500,fill='saddle brown',outline='green',width=4)
           
go = 1
x = 300
y = 50
x1 = 255
x2 = 335
y1 = 480
y2 = 465

zem()
bosorky()

