pprompt ="--> "


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
    print ("Enter number please")
    length = int(input(pprompt))
    k = length - 1
    pyramid(length)
    

while flag:
    take_input()
    print("Press 'Q' to exit.")
    newFlag = str.upper(input(newFlag)) 
    if newFlag =='Q':
        flag = False
    else:
        print("Idiot option tho barabar dal")    
    newFlag=" "           