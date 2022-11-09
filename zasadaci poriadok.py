import tkinter
canvas = tkinter.Canvas()
canvas.pack()


def poriadok(suradnice):
    x = suradnice.x
    y = suradnice.y
    canvas.create_oval(x-10, y-10, x+10, y+10)
    canvas.create_rectangle(x-10, y+10, x+10, y+40)
    canvas.create_text(x,y+60,text=entry1.get())        







entry1 = tkinter.Entry()
entry1.pack()
canvas.bind('<Button-1>',poriadok)
