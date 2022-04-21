nbRanger = int(input("Enter triangle's height:"))

def drawTriangle(n):
    for i in range (1,n+1):
        for j in range (1,n*2):
            if j == n -i+1:
                print("/", end="")
            elif j == n+i:
                print("\ ", end="")
            elif i == n :
                print("_", end="")
            else :
                print(" ", end="")
        if i == n:
            print('\ ')
        print()

drawTriangle(nbRanger)