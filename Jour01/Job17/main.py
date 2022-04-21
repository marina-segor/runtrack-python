for i in range(1, 101):
    resultat = ""
    if i%3 == 0:
        resultat += "Fizz"
    if i%5 == 0:
        resultat += "Buzz"
    if i%3 != 0 and i%5 != 0:
        resultat = i
    print(resultat)