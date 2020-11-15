from tkinter import *
from tkinter import filedialog
root=Tk()
root.filename=filedialog.askopenfile(initialdir="../calculator",title="Select A file",filetypes=(("png file","*.png"),("all files","*.*")))
my_label=Label(root,text=root.filename).pack()
root.mainloop()