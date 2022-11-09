import tkinter
canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()

canvas.create_rectangle(0,450,500,500,fill='blue')
def obrazok(suradnice):
    x = suradnice.x
    y = suradnice.y
   
    if y>450:
        canvas.create_polygon(x+20,y, x-20,y, x-30,y-20, x+30,y-20,fill='white',outline='black',width = 2)
        canvas.create_line(x,y-70,x,y-20,fill='black',width = 2)
        canvas.create_polygon(x,y-20, x+20,y-20, x,y-70,fill='white',outline='black',width=2)

    if y<430:
        canvas.create_oval(x-20,y-20,x+20,y+20,fill='blue')
        canvas.create_line(x-18,y+10,x,y+50,fill='black')
        canvas.create_line(x+18,y+10,x,y+50,fill='black')
        canvas.create_rectangle(x-10,y+50,x+10,y+70,fill='red')   

canvas.bind('<Button-1>',obrazok)
