


prompt = "-->"

print("Hello Welcome")
print("This is a triangle printer")

print("Input the length of the triangle(IN NUMBERS)")
Length = int(input(prompt))

print("printing", Length, "rows")

def triangle(Length):
    for i in range(0, Length):
        for j in range(0, i+1):
            print("# ",end="") 
        print("\n")  

triangle(Length)



