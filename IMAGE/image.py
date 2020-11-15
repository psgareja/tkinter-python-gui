from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("Hakcer")
root.iconbitmap('h.ico')


my_img=ImageTk.PhotoImage(Image.open("h.ico"))
my_label=Label(image=my_img).pack()
button_quit=Button(root,text="Quit",command=root.quit)
button_quit.pack()

root.mainloop()