nombreEntier = int(input("Entrez un nombre : "))

def factorisation(n):

    if(n <= 1):
        return 1
    else:
        return n * factorisation(n-1)
print(factorisation(nombreEntier))