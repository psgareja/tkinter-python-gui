from tkinter import *
root=Tk()
e=Entry(root)

e.pack()
def myClick():
    myLabel=Label(root,text=e.get())
    myLabel.pack()
myButton=Button(root,text="Enter Your name",command=myClick).pack()
root.mainloop()