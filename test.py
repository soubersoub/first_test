import pandas as pd 

def number(a, b):
    
    return a + b


def divise(a, b):
    
    return a / b



def soustraction(c, d):
    if c > d:
        resultat = c - d
        return resultat
    else:
        print(f"{d} est supérieur ou égal à {c}, le résultat sera négatif ou nul.")
        resultat = c - d
        return resultat


def main():
    
    a = 5
    b = 3

    c = 1
    d = 4

    result = soustraction(c,d)

    resultat = number(a, b)

    div = divise(a,b)
    
    print(f"La somme de {a} et {b} est : {resultat}")
    print (result)



if __name__ == "__main__":
    main()
