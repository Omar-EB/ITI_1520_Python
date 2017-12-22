# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
     
     donneur=[]
     autre=[]


     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     for i in range (0,len(p)):
         if i % 2 == 0 :
             donneur.append(p[i])
         else :
             autre.append(p[i])

     
     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat=[]


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI

    trash1=[] # trash1 et trash2 sont de listes qui vont contenir les paires dont on a besoin de s'en debarasser
    trash2=[]
    PremierLettre=[] # PremierLettre et LettreTriple vont etre utilisee pour s'assurer qu'un triplet ne s'elimine pas, et donc si on a 3 cartes avec des nombres/caracteres similaires, le programme eliminera juste 2 et preservera la troisieme
    LettreTriple=[]
    m = l.copy() #copie de la liste qui est remise par l'utilisateur


    for a in range (0, len(m)):                     #ce for loop passe par tous les elements de la liste
        for b in range (0,len(m)):                      #ce for loop compare chaque element avec les autres
            if b != a :                                     #pour qu'un meme elemnt ne soit comparee a lui meme
                if (m[a] != 'J\u2660') and (m[b] != 'J\u2660'): #pour que le pouilleux ne soit jamais eliminee
                    if (m[a])[0] == (m[b])[0]:                      #Si le premier caractere de deux ou trois ou quatres cartes est le meme, on sait qu'on a soit un pair, soit un triplet soit un quatrulplet
                            trash1.append(a)                            #ajoute le numero des index qui signifient le paire ou le triplet ou le quatruplet

  
    for c in list(set(trash1)): #on utilise list set pour eleminer toutes les repititions qui se produisent en trash1
        trash2.append(m[c]) #on cherche les positions de la liste m qui signifient au paires et on ajoute les valeurs des paires au liste trash2 

    for d in trash2 :
        PremierLettre.append(d[0]) #on cherche les premieres lettres de chacunes d'element de trash2 pour savoir s'il y a un qui se repete 3 fois

    for lettre in PremierLettre :
        if PremierLettre.count(lettre) == 3 :
            LettreTriple.append(lettre)#si un lettre se repete 3 fois, on le note

    u=[] # une liste qui va permettre de stocker les positions des index qui siginifient a un membre du triplet
    for lettretriple in list(set(LettreTriple)): #evite la repitition de la lettre
        u.append(PremierLettre.index(lettretriple))

    val=[] #une liste qui permet de stocker les valeurs de cahque element de la liste u
    for positionlettretriple in u :
        val.append(trash2[positionlettretriple])

    for w in val:
        trash2.remove(w)     #cela va enlever une des 3 duplications de la meme lettre de trash2, donc elle ne s'eleminera pas et seule le paire qui reste va s'eleminer

    for e in trash2:
        m.remove(e) #on ordonne l'ordinateur d'enlever tous les objets dans m qui sont similaires a ceux qui sont dans trash2
        
    resultat = m #la liste sans les paires

    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    a=''
    for i in p :
        a+= i+' '
    print (a)

    

def entrez_position_valide(n):
     '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
     '''

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     a = True
     while a :
        v = int(input("J'ai "+str(n)+" cartes, si 1 est la position de ma première carte et "+str(n)+" est la position de ma dernière carte, laquelle de mes cartes voulez-vous avoir?"))
        if v in range (1, n+1):
            a = False
            return v
        else:
            a = True
            print ("Position invalide, veuillez ressayer une autre fois.")
            
     

def joue():
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet()
     melange_paquet(p)
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]

     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
     attend_le_joueur()
     
     donneur=elimine_paires(donneur)
     humain=elimine_paires(humain)

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     print("Après vous être débarrassé de toutes les paires et mélangé les cartes, votre main est: ")
     affiche_cartes(humain) #pour que le joueur connait exactement ses cartes apres l'elemination des paires
     for i in range (0,9999): #celui-ci est un domaine assez grand pour finir le jeu
         print ("**************************************************************************")
         if i % 2 == 0:  #nombre pair, tour du robot
             if len(donneur) > 0 : #si le robot n'a pas deja gagne
                print ("Mon tour")
                m= random.randint(0,len(humain)-1) #un nombre aleatoire entre 0 et la taille de nombre de cartes de l'humain-1
                donneur.append(humain[m]) #on ajoute a robot l'element signifiant
                humain.remove(humain[m]) #on enleve de humain l'element signifiant
                donneur=elimine_paires(donneur) #elemination des paires
                if m == 0: #cette condition est juste mise en oeuvre pour des raison de coherence linguistique, pas pour jouer un role dans le prog.
                    print("j'ai pris votre",m+1,"ère carte.") 
                else :
                    print("j'ai pris votre",m+1,"ème carte.")
                attend_le_joueur()
             if len(donneur) == 0 : #le robot a gagnee
                return (print("J'ai terminé toutes mes cartes, et vous avez le Pouilleux! (J♠). Vous avez perdu! Moi, Robot, J'ai gagné! "))
                
            
            
         if i % 2 != 0:  #nombre impair, tour de l'humain
            if len(humain) > 0 : #si l'humain n'a pas deja gagne
                print ("Votre tour")
                print ("Votre main est")
                affiche_cartes(humain)
                s = entrez_position_valide(len(donneur)) #choix par l'utilisateur quelle carte il veut
                if s > 1: #cette condition est juste mise en oeuvre pour des raison de coherence linguistique, pas pour jouer un role dans le prog.
                    print("Vous avez demandé ma",s,"ème carte.")
                if s == 1:
                    print("Vous avex demandé ma",s,"ère carte.")
                print("La voilà, c'est un ",donneur[s-1]) #affichage de la carte qui signifie le nombre que l'utilisateur a choisit
                humain.append(donneur[s-1]) #on ajoute la carte a la liste des cartes de l'utilisateur
                print("Avec ",donneur[s-1]," ajoutée, votre main est")
                affiche_cartes(humain)
                donneur.remove(donneur[s-1]) #on enleve de robot l'element signifiant
                print("Après vous être débarrassé de toutes les paires et mélangé les cartes, votre main est: ")
                humain=elimine_paires(humain)
                affiche_cartes(humain)
                attend_le_joueur()
            if len(humain) == 0 : #l'utilisateur a gagnee
                return (print("Vous avez terminé toutes les cartes et moi, Robot, J'ai le Pouilleux (J♠). Félicitations! Vous, Humain, avez gagné."))

            
            

        
    

	 
# programme principale
joue()

