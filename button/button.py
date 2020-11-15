from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Button")
#r=IntVar()
#r.set("2")
MODES=[
    ("Pepperoni","Pepperoni"),
    ("cheese","cheese"),
    ("mushroom","mushroom"),
    ("onion","onion")
]

pizza=StringVar()
pizza.set("Pepperoni")
for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

def clicked(value):
    Label(root,text=value).pack()

#Radiobutton(root,text='option1',variable=r,value=1,command=lambda:clicked(r.get())).pack()
#Radiobutton(root,text='option2',variable=r,value=2,command=lambda:clicked(r.get())).pack()
Button(root,text='click',command=lambda:clicked(pizza.get())).pack(anchor=W)

mainloop()