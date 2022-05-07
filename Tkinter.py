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
top.geometry("570x600")
top.title("Colour changer")

redbut = Button(top, text="Red", fg="red", font='Helvetica 14 bold', command=redbg, padx=40, pady=40)
redbut.pack(side=RIGHT)

blubut = Button(top, text="Blue", fg="blue", font='Helvetica 14 bold', command=blubg, padx=40, pady=40)
blubut.pack(side=RIGHT)

grenbut = Button(top, text="Green", fg="green", font='Helvetica 14 bold', command=grenbg, padx=40, pady=40)
grenbut.pack(side=RIGHT)

blakbut = Button(top, text="Black", fg="black", font='Helvetica 14 bold', command=blakbg, padx=40, pady=40)
blakbut.pack(side=RIGHT)

top.mainloop()
