def pyramid_even(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')
    __prompt = "--->"
    n = int(input(__prompt))
    l = n - 1
    e = 0
    for i in range(0, n):     # no of lines
        for j in range(0, l): # no of spaces
            print(end="  ")
        l = l - 1

        for k in range((i + 1) +e):   #triangle
            print("* ", end="")

        print("\r")
        e = e + 1


if __name__ == '__main__':
    pyramid_even('Welcome to the pyramid code')

