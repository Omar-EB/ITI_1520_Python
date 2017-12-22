def exercice(): #Ex3
    print("Ce logiciel va vous tester avec 10 questions")
    import random
    while (True): #Ce while loop est pour verifier que l'eleve admet soit 0 soit 1 et rien d'autre
        choix = int(input("Voulez vous faire la multiplication (1) ou bien l'addition (0)? "))
        if choix == 1 : #choix de multiplication
            print("SVP donner les reponses aux multiplications suivantes:")
            a = [] #la liste qui signifie le nombre de fois l'eleve a eu la bonne reponse
            for i in range(1, 11):  #Exactement 10 questions
                entier1 = int(9*(random.random())+1)
                entier2 = int(9*(random.random())+1)
                n = entier1 * entier2
                print("question",i,":", entier1,"x",entier2,"=") 
                rep = int(input())#la reponse de l'eleve
                if rep != n :
                    print("Incorrect,", entier1,'x', entier2, '=', n)
                else :
                    a.append(1)
            if (len (a)) > 6 :
                print("Felicitations!", len(a), "reponses correctes.")
            else:
                print(len(a), "reponses correctes, demandez de l'aide a votre enseignant(e).")
        elif choix == 0 :  #choix d'addition
            print("SVP donner les reponses aux additions suivantes:")
            a = [] #la liste qui signifie le nombre de fois l'eleve a eu la bonne reponse
            for i in range(1, 11): #Exactement 10 questions
                entier1 = int(9*(random.random())+1)
                entier2 = int(9*(random.random())+1)
                n = entier1 + entier2
                print("question",i,":", entier1,"+",entier2,"=")
                rep = int(input()) #la reponse de l'eleve
                if rep != n :
                    print("Incorrect,", entier1,'+', entier2, '=', n)
                else :
                    a.append(1)
            if (len (a)) > 6 :
                print("Felicitations!", len(a), "reponses correctes.")
            else:
                print(len(a), "reponses correctes, demandez de l'aide a votre enseignant(e).")
        else: #si un nbre autre que 0 et 1 a ete soumis, le while loop va redemander la question du depart
            print ("1 et 0 sont les seules valeurs acceptees.")
