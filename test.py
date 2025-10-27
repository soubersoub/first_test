import pandas as pd 

def number(a, b):
    
    return a + b

<<<<<<< HEAD
def produit(a, b):
    
    return a * b
=======

def divise(a, b):
    
    return a / b


def calcule_age( age ):

    v = 2025 - age 
    print(f"votre age est {v} ans")

    return v
    

>>>>>>> hotfix


def soustraction(c, d):
    if c > d:
        resultat = c - d
        return resultat
    else:
        print(f"{d} est supérieur ou égal à {c}, le résultat sera négatif ou nul.")
        resultat = c - d
        return resultat


def main():
<<<<<<< HEAD
    
=======
    age1 = 1996
>>>>>>> hotfix
    a = 5
    b = 3

    c = 1
    d = 4

    result = soustraction(c,d)
<<<<<<< HEAD

    resultat = number(a, b)

    resu = produit( a,b )
    
    print(f"La somme de {a} et {b} est : {resultat}")
    print (result)
    print (resu)
=======
    resultat = number(a, b)
    div = divise(a,b)
    age_test = calcule_age(age)


    
    print(f"La somme de {a} et {b} est : {resultat}")
    print (result)
    print ( age_test)
>>>>>>> hotfix



if __name__ == "__main__":
    main()
