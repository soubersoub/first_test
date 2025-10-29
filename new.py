import pandas as pd

import tqdm as td 

import math 


def number(a, b):
    v= a+ b
    return v 

def calcul_age(age):
    calc = 2025 - age
    return calc 

def main():
    a = 5
    b = 3
    resultat = number(a, b)
    print(resultat)

    ages = 1996

    test_age = calcul_age(ages) 
    print(f"Votre age est {test_age}")


if __name__ == "__main__":
    main()