def sequenceMax(x):
     '''(list)-> int
     cette focntion prend une liste de nombres et retourne
     la longueur de la plus longue séquence des éléments consécutive égaux 
      '''
     i = 0
     maxL = 1
     while i < len(x)-1 :
        tempL = 1
        while  i < len(x)-1 and x[i] == x[i+1]:
           tempL = tempL + 1
           i = i + 1
        if tempL > maxL:
           maxL = tempL  
        i = i + 1   
     return maxL

s = input("Veuillez entrer une liste des valeurs séparées par virgules: ")
a = list(eval(s))
print(sequenceMax(a))





