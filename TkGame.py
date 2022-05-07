import time
from tkinter import messagebox
from tkinter import *
import threading

money = 0.0
Invests: float = 0
Invests_money = 0.0
time0 = 0
stopInvest: bool = True
count = 0
countlocal = 0
total_money = 0


def timepas():
    global time0
    global money
    global total_money
    global Invests
    global Invests_money
    global stopInvest
    global countlocal
    while stopInvest:
        countlocal = countlocal + 1
        Invests_money = Invests * 2
        money = money + Invests_money
        print(money)
        time.sleep(1)
        if countlocal == count:
            stopInvest = False
        continue



def work_money():
    global money
    money += 1


def BankAcc():
    global money
    messagebox.showinfo("Your Bank Account", "You have $:" + str(total_money))


def Inves():
    global Invests
    global money
    if money >= 10:
        Invests = Invests + 1
        money = money - 10
        print("Invested")
        print("Now you have $:", money)
        print("You have ", Invests, " Invests")
        print()
        timepas()
    elif money < 10:
        print("You don't have enough money.")
        print("Tip:Press work to get more money")


def stop_investing():
    global count
    global countlocal
    global total_money
    global money

    count = 10
    countlocal
    total_money = total_money + money


# Threads
#p = threading.Thread(target=timepas)
#p.start()

# tkinter stuff
gamesc = Tk()
gamesc.title("Clickathon")
gamesc.geometry("480x270")
gamesc.iconbitmap('F:/GIT_REPO/python/python/TkGame.ico')

work = Button(text="Work", command=work_money)
work.pack(side=TOP, ipadx=20, ipady=20)

CkBankAcc = Button(text="Check Bank Account", command=BankAcc)
CkBankAcc.pack(side=BOTTOM)

# I can't figure this out Help me

ShareMar = Button(text="Invest in Shares", command=Inves)
ShareMar.pack(side=LEFT)
ShareMar1 = Button(text="Invest for 10 Years", command=stop_investing)
ShareMar1.pack(side=RIGHT)

gamesc.mainloop()
