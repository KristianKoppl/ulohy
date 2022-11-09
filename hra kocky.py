import tkinter
from random import*
canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()





a_kocka=0
b_kocka=0
def obrazok():
    global a_kocka, b_kocka
    canvas.delete('all')
    canvas.after(1000,obrazok)
    canvas.create_rectangle(200,250,250,300,fill='red')
    canvas.create_rectangle(260,250,310,300,fill='blue')
    a_kocka=randrange(1,7)
    b_kocka=randrange(1,7)
    canvas.create_text(225,275,text=a_kocka, font='Arial 20')
    canvas.create_text(285,275,text=b_kocka, font='Arial 20')
    canvas.create_text(200,150,text='Počet bodov je:',font='Arial 30')
    canvas.create_text(365,150,text=body,font='Arial 50')

body = 0 
def rovnake():
    global body
    if a_kocka == b_kocka:
        body += 2
    else:
        body -= 1
        
    
    
    

obrazok()



    



button1 = tkinter.Button(text='rovnaké!',command=rovnake)
button1.pack()
