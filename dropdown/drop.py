from tkinter import *

root=Tk()
clicked=StringVar()
clicked.set('one')


def show():
    opetion=[
        'one',
        'two',
        'three',
        'faour'
    ]
    drop=OptionMenu(root,clicked,*opetion)
    drop.pack()

mybtn=Button(root,text='selection',command=show).pack()
root.mainloop()