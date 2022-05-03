from tkinter import *

def redbg():
    top.configure(bg='red')

def blubg():
    top.configure(bg='blue')

def grenbg():
    top.configure(bg='green')

def blakbg():
    top.configure(bg='black')

top = Tk()
top.geometry("600x600")
redbut = Button(top, text="Red", fg="red", font='Helvetica 10 bold', command=redbg,padx = 50, pady = 50)
redbut.pack(side=LEFT)

blubut = Button(top, text="Blue", fg="blue", font='Helvetica 10 bold', command=blubg,padx = 50, pady = 50)
blubut.pack(side=TOP)

grenbut = Button(top, text="Green", fg="green", font='Helvetica 10 bold', command=grenbg,padx = 50, pady = 50)
grenbut.pack(side=RIGHT)

blakbut = Button(top, text="Black", fg="black", font='Helvetica 10 bold', command=blakbg,padx = 50, pady = 50)
blakbut.pack(side=BOTTOM)

top.mainloop()

