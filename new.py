
import numpy as np 

import pandas as pd

import tqdm as td 



def number(a, b):
    v= a+ b
    return v 


def prenom(nom):
    b = nom

    return b 

def capital(pays):
    payss = pays

    return payss

def calculatrice (num):

    test_calulatrice = num

    return test_calulatrice


def calcul_age(age):
    calc = 2025 - age
    return calc 


def main():
    a = 5
    b = 3
    resultat = number(a, b)
    print(resultat)


    noms = prenom("SOUBER OMAR")
    print (noms)

    ages = 1996

    test_age = calcul_age(ages) 
    print(f"Votre age est {test_age}")



if __name__ == "__main__":
    main()