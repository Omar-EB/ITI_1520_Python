def compte_pos(x):
     '''(list)->int
      Retourne le nombre des elements positifs
      '''
     compteur = 0
     i = 0
     while i < len(x):
        if x[i] > 0 :
          compteur = compteur + 1
        i = i + 1   
     return compteur


s = input('Veuillez entrer une liste des valeurs séparées par virgules: ')
a = list(eval(s))
print(compte_pos(a))






