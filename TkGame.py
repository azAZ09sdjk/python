from tkinter import messagebox
from Tkinter import *
import time

money = 0
Invests: int = 0

def work_money():
    global money
    money += 1


def BankAcc():
    messagebox.showinfo("Your Bank Account", "You have $:"+str(money))


def Inves():
    global Invests 
    Invests = Invests + 1
    


gamesc = Tk()
gamesc.title("Clickathon")
gamesc.geometry("480x270")
gamesc.iconbitmap('F:/GIT_REPO/python/python/TkGame.ico')

work = Button(text="Do work", command=work_money)
work.pack(side=TOP)

CkBankAcc = Button(text="Check Bank Account", command=BankAcc)
CkBankAcc.pack(side=BOTTOM)

#i cant figure this out Help me
if money > 10:
    ShareMar = Button(text="Invest in Shares", command=Inves)
    ShareMar.pack(side = LEFT)

gamesc.mainloop()
