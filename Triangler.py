


prompt = "-->"

print("Hello Welcome")
print("This is a triangle printer")

print("Input the length of the triangle(IN NUMBERS)")
Length = int(input(prompt))

print("printing", Length, "rows")

def triangle(Length):
    for abc in range(0, Length):
        for jcb in range(0, abc+1):
            print(" * ",end="") 
        print("\n")  

triangle(Length)



