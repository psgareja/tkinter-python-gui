from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("window")
def open():
    global my_img
    top=Toplevel()

    lbl=Label(top,text='hello world').pack()
    my_img=ImageTk.PhotoImage(Image.open('h.ico'))
    my_label=Label(top,image=my_img).pack()

btn=Button(root,text="open",command=open).pack()

root.mainloop()
