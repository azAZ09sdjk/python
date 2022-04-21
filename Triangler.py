


prompt = "-->"

print("Hello Welcome")
print("This is a triangle printer")

print("Input the length of the triangle(IN NUMBERS)")
Length = int(input(prompt))

print("What type of triangle do you want(int or str)")
TriType =input(prompt)

if TriType == "str":
    print("What would the string be (enter anything other than numbers)")
    strtp = input(prompt)

print("printing", Length, "rows")


if TriType == "str" :
    def triangleNor(Length):
        for abc in range(0, Length):
            for jcb in range(0, abc+1):
                print(strtp, end=" ") 
            print("\n")

if TriType == "int":
    def triangleNum(length):
        for bcd in range(0, Length + 1):
            for op in range(0, bcd):
                print (bcd , end = " ")
            print("\n")

if TriType == "str":
    triangleNor(Length)

if TriType == "int":
    triangleNum(Length)


