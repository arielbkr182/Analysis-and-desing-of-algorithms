from tkinter import *
root=Tk()
miframe=Frame(root, width=500, height=400)
miframe.pack()
miImagen=PhotoImage(file="2504618.png")
Label(miframe, image=miImagen).place(x=100, y=200)
root.mainloop()