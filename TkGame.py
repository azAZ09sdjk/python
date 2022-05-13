
#VERY MUCH INCOMPLETE DOSENT WORK!


from tkinter import messagebox
from tkinter import *


money = 0
Plants = 0
PlantCost = 10
Chair = 0
ChairCost = 1000
MoneyPerWork = 1

def work_money():
    global money
    money = money + MoneyPerWork


def BankAcc():
    global money
    messagebox.showinfo("Your Bank Account", "You have $:" + str(money))

def Plant():
    global Plants
    global MoneyPerWork
    global PlantCost
    global money
    if PlantCost < money:
        Plants = Plants+1
        MoneyPerWork = MoneyPerWork + 1
        money = money-PlantCost
        PlantCost = PlantCost * 1.5
        PlantCost = int(PlantCost)
        PlantCost.__round__
        mwm1.config(text="Buy Plant $:" + str(PlantCost), command=Plant)


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

mwm1 = Button(text="Buy Plant $:" + str(PlantCost), command=Plant)
mwm1.pack(side=LEFT)

mwm2 = Button(text="Buy Chair $:" + str(ChairCost), command=Chair)



gamesc.mainloop()

list4 = [12, 1.23, 69, "Funny number", False]
print(list4)


while money == 1000 or money > 1000:
    mwm2.pack(side=LEFT, pady=20)
    continue