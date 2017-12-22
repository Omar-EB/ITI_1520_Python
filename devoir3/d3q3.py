def sequence_Max(): #Ex 3
    l= input("Veuillez rentrer les valeurs de la liste separes par des virgules")
    L= list(eval(l))
    a=1
    t=[]
    for i in range (0, len(L)-1):   
            if L[i] == L[i+1] : #a=1, et chaue fois qu'un element va etre egale a le suivant, on ajoute 1 a (a) et donc a signifie maintentant le nombre de fois l'elemnt se repete
                a += 1
            if L[i] != L[i+1] : #lorsque deux elemnt consecutifs ne sont pas egaux, (a) est reinitialisee a 1
                a = 1
            t.append(a) #on ajoute toutes les valeurs de (a) qu'on obtient dans cette liste et on imprime la valur maximale
    print(max(t))
