#Ex4
# la partie a :
def partieA(q):
    import random
    if q == 1 : #choix de multiplication
        print("SVP donner la reponse a la multiplication suivante:")
        entier1 = int(9*(random.random())+1)
        entier2 = int(9*(random.random())+1)
        n = entier1 * entier2
        print(entier1,"x",entier2,"=")
        rep = int(input()) #la reponse de l'eleve
        if rep != n :
            print("Incorrect,", entier1,'x', entier2, '=', n)
            return False
        else:
            return True
    if q == 0 :  #choix d'addition
        print("SVP donner la reponse a l'addition suivante:")
        entier1 = int(9*(random.random())+1)
        entier2 = int(9*(random.random())+1)
        n = entier1 + entier2
        print(entier1,"+",entier2,"=")
        rep = int(input()) #la reponse de l'eleve
        if rep != n :
            print("Incorrect,", entier1,'+', entier2, '=', n)
            return False
        else:
            return True

#la partie b :
def exercice2() :
    import random
    a=[]
    print("Ce logiciel va vous tester avec 10 questions")
    for i in range (1, 11) :
        n1 = int(2*random.random()) #Cela fait en sorte que n1 soit egal a 0 ou 1 aleatoirement
        print ("question",i,":")
        if partieA(n1) == True :
            a.append(1)

    if (len (a)) > 6 :
            print("Felicitations!", len(a), "reponses correctes.")
    else:
        print(len(a), "reponses correctes, demandez de l'aide a votre enseignant(e).")
            
