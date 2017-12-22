def ajoute():
    L=[]
    m = str(input("rentrer les valeurs de la matrice/liste separee par espaces:\n"))
    L.append(list(map(int,m.split(' '))))
    x = ' '
    while x is not ('') :
        x= str(input())
        if x is not (''):
            L.append(list(map(int,x.split(' '))))
    # L est la matrice ou liste principale
    print ('La matrice avant la modification est',L)
    for ligne in range (len(L)):
        for colonne in range (len(L[ligne])):
            L[ligne][colonne] = L[ligne][colonne] + 1
    print ('La matrice apres la modification est',L)
    return (L)
def ajouteV2(L):
    new=[] #nouvelle matrice qui va etre affichee
    for i in range (len(L)):
        new.append([]) #ajoute les lignes dans la liste a afficher
    for ligne in range (len(L)):
        for colonne in range (len(L[ligne])):
            new[ligne].append(L[ligne][colonne] + 1)
    print ("la matrice donne est",L)
    print ("la nouvelle matrice creee apres l'execution de la focntion ajouteV2 est",new)
    
#Programme principale:
ajouteV2(ajoute())
