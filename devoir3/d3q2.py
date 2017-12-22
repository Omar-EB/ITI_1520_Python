def sequenceDesDeux(): #Ex 2
    l= input("Veuillez rentrer les valeurs de la liste separes par des virgules")
    L= list(eval(l))
    a=0
    for i in range (0, len(L)-1):
        if  L[i] == L[i+1] : #si un element de la liste est egale a celui qui le suit, on ajoute 1 a (a)
            a += 1
    if a >= 1 : #si a>=1, on sait qu'il y a au moins une sequence de 2 nombres egaux
        return True
    else:
        return False
