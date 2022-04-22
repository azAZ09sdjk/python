


def pyramid(length):
    k = length
    for i in range(0, length+1):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i):
            print("*", end= " ")
        print("\n")

flag = True
newFlag = "" 
def take_input():
    prompt = "Enter number please -->"
    length = int(input(prompt))
    k = length - 1
    pyramid(length)
    

while flag:
    take_input()
    print("Do you want to continue..[y/n]-->")
    newFlag = str(input(newFlag)) 
    if newFlag =='y':
        flag = True
    else: 
        flag = False
    newFlag=" "           