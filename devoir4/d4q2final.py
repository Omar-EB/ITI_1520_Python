def effaceTableau (tab):
   '''
   (list) -> None
   Cette fonction prepare le tableau de jeu (la matrice) 
   en mettant '-' dans tous les elements.
   Elle ne crée pas une nouvelle matrice
   Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab[i][j]="-"
def afficheTableau (tab):
    '''
    (list) -> None
    Affiche le tableau de jeu
    Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    Le format est: 
        0 1 2
      0 - - O
      1 - X -
      2 - - X
    '''
    print("   ", end="")
    col = 0
    while col < len(tab): 
      print(col, end="  ")
      col += 1
    print()  
    row = 0  
    while row < len(tab):  
      print(row, end="")
      col = 0
      while col < len(tab[row]): 
        print(" ",tab[row][col], end="")
        col += 1
      print()
      row += 1

def joue (tab, joueur):
    '''
    (list, str) -> None
    Joue une étape de jeu
    Preconditions: tab is a reference to the n x n tab containing '-', 'X' and 'O'
    Le joueur est X ou O
    tab est modifié (un element est changé)
    '''               
    
    valid = False
                 
    while not valid:   
        place = [-1,-1] 
        while not((0 <= place[0] < len(tab)) and (0 <= place[1] < len(tab))):
          print ("Joueur ",joueur, end="")
          print(", donnez la ligne et la colonne de 0 à", (len(tab)-1), ": ")
          place[0] = int(input("Ligne: ")) 
          place[1] = int(input("Colonne: "))
               
        if tab[place[0]][place[1]] != '-':
          print("position", place[0], place[1], " occupée");
          valid = False
        else:
          valid = True             
      
          tab[place[0]][place[1]] = joueur

            
    
      
def verifieGagner(tab):  
    '''(list) ->  bool
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    * Verifie s'il y a un gagnant.
    * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
    * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!" 
    * ou "Joueur O a gagné!") et retourne True.
    * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
    * affiche "Match nul" et retourne True.
    * Si le jeu n'est pas fini, retourne False.
    * La fonction appelle les fonctions testLignes, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas de gagnant
    '''
    gagnant = testLignes(tab)
    if gagnant == "-": 
        gagnant = testCols(tab)
        if gagnant == "-":
            gagnant = testDiags(tab)
            if gagnant == "-": 
                gagnant = testMatchNul(tab)
                if gagnant == True: 
                    print("Match Nul (egalitée)")
    if gagnant == "-":
        print()
    if gagnant == False:
        print()
    elif gagnant != "-":
        print( gagnant, " est le gagnant")
        return gagnant
        

 
def testLignes(tab):
   ''' (list) ->  str
   * verifie s’il y a une ligne gagnante.
   * cherche trois 'X' ou trois 'O' dans une ligne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   i=0
   j=0
   for i in range(len(tab)):
        if tab[i][j]==tab[i][j+1] and tab[i][j+1]==tab[i][j+2]: 
            if tab[i][j]=="X": 
                return "X"
            elif tab[i][j]=="O":
                return  "O"
        return "-"
  
  
def testCols(tab):
   ''' (list) ->  str
   * verifie s’il y a une colonne gagnante.
   * cherche trois 'X' ou trois 'O' dans une colonne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   i=0
   j=0
   for j in range(len(tab)):
        if tab[i][j]==tab[i+1][j] and tab[i+1][j]==tab[i+2][j]:
            if tab[i][j]=="X":
                return "X"
            elif tab[i][j]=="O":
                return "O"
   return "-"
   
def testDiags(tab):
   ''' (list) ->  str
   * cherche trois 'X' ou trois 'O' dans une diagonale.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné
   * sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''

   if tab[0][0]==tab[1][1]and tab[1][1]==tab[2][2]: 
        if tab[0][0]=="X": 
            return "X"
        elif tab[0][0]=="O":
            return "O"
   elif tab[2][0]==tab[1][1] and tab[1][1]==tab[0][2]: 
         if tab[2][0]=="X":
            return "X"
         elif tab[2][0]=="O":
            return "O"
   return "-"
  
  
def testMatchNul(tab):
   ''' (list) ->  bool
   * verifie s’il y a un match nul
   * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.  
   * Si on ne trouve pas de '-' dans la matrice, retourne True. 
   * S'il y a de '-', retourne false.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
   for i in range(len(tab)):
        for j in range(len(tab[i])):
            if str(tab[i][j])=="-": 
                return False
            elif i==2 and j==2:
                if str(tab[i][j])!="-": 
                    return True
   return False
       
tableau = [['-','-','-'],['-','-','-'],['-','-','-']] 
    
reponse = input("Commencez a jouer en apuillant (O)ou (N)si vous ne voulez pas commencer maintenant : ");    
while reponse == 'o' or reponse == 'O': 
      effaceTableau(tableau) 
      gagnant = False   
      while not gagnant: 
        afficheTableau(tableau) 
        joue(tableau,'X')  
        gagnant = verifieGagner(tableau)  
        if not gagnant: 
          
          afficheTableau(tableau) 
          joue(tableau,'O')  
          gagnant = verifieGagner(tableau)  
          
      afficheTableau(tableau) 
      reponse = input("Commencez a jouer en apuillant (O)ou (N)si vous ne voulez pas commencer maintenant: ") #jouer a nouveau?

