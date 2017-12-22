import random

def effectuezTest(operation): 
    resultat = False
    num1 = random.randint(0,9)
    num2 = random.randint(0,9) 
    if operation == 0: 
          reponse = int(input(str(num1) + " + " + str(num2) + " = "))
          somme = num1 + num2
          if somme == reponse :
            resultat = True
          else: 
            print("Incorrect – la reponse est", somme)
    else:  
          reponse = int(input(str(num1) + " * " + str(num2) + " = "))
          mult = num1 * num2
          if(mult == reponse):
            resultat = True
          else: 
            print("Incorrect – la reponse est", mult)
    return resultat
    
reponsesCorrectes = 0
print("Ce logiciel va effectuez un test avec 10 questions …… ");
for compteur in range (10):
    operation = random.randint(0,1)
    if effectuezTest(operation) == True:
         reponsesCorrectes += 1
print(reponsesCorrectes, "reponses correctes.")         
if reponsesCorrectes  <= 6 :
  print("Demandez à votre enseignant(e) pour de l’aide.")
else:
  print("Felicitations!")
