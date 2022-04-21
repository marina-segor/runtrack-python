lignes = int(input("Enter width : "))
colonnes = int(input("Enter height : "))

def drawRectangle (a, b):
    for i in range(1,a+1):
        for j in range(1,b+1):
            if j == 1 or j == b:
                print(" | ", end="")
            elif i == 1 or i == a:
                print("-", end="")
            else:
                print(" ", end="")
        print()

drawRectangle(colonnes,lignes)


