import numpy as np 

def soustraction(c, d):
    if c > d:
        resultat = c - d
        return resultat
    else:
        print(f"{d} est supérieur ou égal à {c}, le résultat sera négatif ou nul.")
        resultat = c - d
        return resultat