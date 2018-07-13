
print("1 = ADD","2 = SUBSTRACT","3 = MULTIPLY","4 = DIVIDE",sep = "\n")

def calculator():
    z = int(input("Chose your task"))

    if(z == 1):
        x = int(input("Enter your Numbers"))
        y = int(input("Enter your second Numbers"))
        print (x)
        print (y)
        a = x + y
        return a

    if(z == 2):
        x = int(input("Enter your Numbers"))
        y = int(input("Enter your second Numbers"))
        print(x)
        print(y)
        b = x - y
        return b

    if(z == 3):
        x = int(input("Enter your Numbers"))
        y = int(input("Enter your second Numbers"))
        print(x)
        print(y)
        c = x * y
        return c

    if(z == 4):
        x = int(input("Enter your Numbers"))
        y = int(input("Enter your second Numbers"))
        print(x)
        print(y)
        d = x / y
        return d

    else:
        print("You have chose the wrong option")

i = calculator()
print(i)
