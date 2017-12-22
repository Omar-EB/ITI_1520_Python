def compte_pos(): #Ex 1 
    l= input("Veuillez rentrer les valeurs de la liste separes par des virgules")
    L= list(eval(l))
    a=0
    somme = 0
    while a < len(L) :
        if L[a] > 0 : # tous les elements > 0 sont comptees et 1 est ajoutee a somme
            somme += 1
        a+= 1
    return somme #le nombre d'elements positifs
    print (somme)
