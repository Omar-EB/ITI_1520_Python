def sequenceDesDeux(x):
     '''(list)-> bool
      Retourne true s’il y a au moins une séquence des deux
      éléments consécutive égaux, et False sinon
      '''
     res = False
     i = 0
     while i < len(x) - 1 and not res:
       if x[i]== x[i+1]:
            res = True
       i = i + 1
     return res

s = input("Veuillez entrer une liste des valeurs séparées par virgules: ")
a = list(eval(s))
print(sequenceDesDeux(a))






