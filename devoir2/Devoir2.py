def calculeIMC(): #Ex1
    masse = float(input("Veuillez rentrer votre poids en kilogrammes: "))
    taille = float(input("Veuillez rentrer votre taille en metres: "))
    IMC= masse / (taille*taille)
    print("Votre IMC est: ", IMC,"kg/(m^2)")
    if IMC < 18.5 :
        print("Maigreur")
    elif 18.5 <= IMC and IMC < 25 :
        print("Poids idéal")
    elif 25 <= IMC and IMC < 30 :
        print("Surpoids")
    elif IMC >= 30 :
        print("Obésité")

def AàB(): #Ex2
    a = int(input("Veuillez donner la valeur de a: "))
    b = int(input("Veuillez donner la valeur de b: "))
    for i in range(a, b+1) :
        print (i)

def exercice(): #Ex3
    print("Ce logiciel va vous tester avec 10 questions")
    import random
    while (True): #Ce while loop est pour verifier que l'eleve admet soit 0 soit 1 et rien d'autre
        choix = int(input("Voulez vous faire la multiplication (1) ou bien l'addition (0)? "))
        if choix == 1 : #choix de multiplication
            print("SVP donner les reponses aux multiplications suivantes:")
            a = [] #la liste qui signifie le nombre de fois l'eleve a eu la bonne reponse
            for i in range(1, 11):  #Exactement 10 questions
                entier1 = int(9*(random.random())+1) #nombre entre 1 et 9 inclusivement
                entier2 = int(9*(random.random())+1)
                n = entier1 * entier2
                print("question",i,":", entier1,"x",entier2,"=",end=' ') #demande la question
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
                print("question",i,":", entier1,"+",entier2,"=",end=' ') #demande la question
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

#Ex4
# la partie a :
def partieA(q):
    import random
    if q == 1 : #choix de multiplication
        print("SVP donner la reponse a la multiplication suivante:")
        entier1 = int(9*(random.random())+1)
        entier2 = int(9*(random.random())+1)
        n = entier1 * entier2
        print(entier1,"x",entier2,"=",end=' ') #demande la question
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
        print(entier1,"+",entier2,"=",end=' ') #demande la question
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
            
exercice2()
