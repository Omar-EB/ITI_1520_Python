def compte_pos(): #Ex 1 
    l= input("Veuillez rentrer les valeurs de la liste separes par des virgules")
    L= list(eval(l))
    a=0
    somme = 0
    while a < len(L) :
        if L[a] > 0 :
            somme += 1
        a+= 1
    return somme
    print (somme)
    

def sequenceDesDeux(): #Ex 2
    l= input("Veuillez rentrer les valeurs de la liste separes par des virgules")
    L= list(eval(l))
    a=0
    for i in range (0, len(L)-1):
        if  L[i] == L[i+1] :
            a += 1
    if a >= 1 :
        return True
    else:
        return False


def sequence_Max(): #Ex 3
    l= input("Veuillez rentrer les valeurs de la liste separes par des virgules")
    L= list(eval(l))
    a=1
    t=[]
    for i in range (0, len(L)-1):   
            if L[i] == L[i+1] :
                a += 1
            if L[i] != L[i+1] :
                a = 1
            t.append(a)
    print(max(t))



