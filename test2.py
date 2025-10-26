def number(a, b):
    v= a+ b
    return v 

def prenom (nom):
    
    v = nom 
    return v  

def main():
    a = 5
    b = 3
    resultat = number(a, b)
    print(resultat)

    noms= "SOUBER "
    name = prenom(noms)
    print(name)


if __name__ == "__main__":
    main()