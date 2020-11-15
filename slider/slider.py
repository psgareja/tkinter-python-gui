from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Slider")

verticle=Scale(root,from_=0,to=200)
verticle.pack()
horizontal=Scale(root,from_=0,to=200,orient=HORIZONTAL)
horizontal.pack()
root.mainloop()