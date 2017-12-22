import random

def effectuezTest(operation): 
    compteur = 0
    reponsesCorrectes = 0
    if operation == 0:
        print("SVP donnez les reponses aux additions suivantes:")
        for counter in range(10): 
          num1 = random.randint(0,9)
          num2 = random.randint(0,9)  
          reponse = int(input(str(num1) + " + " + str(num2) + " = "))
          somme = num1 + num2
          if somme == reponse :
            reponsesCorrectes += 1
          else: 
            print("Incorrect – la reponse est", somme)
    else:  
        print("SVP donnez les reponses aux multiplications suivantes:")
        for compteur in range(10):
          num1 = random.randint(0,9)
          num2 = random.randrange(0,9)
          reponse = int(input(str(num1) + " * " + str(num2) + " = "))
          mult = num1 * num2
          if(mult == reponse):
            reponsesCorrectes  += 1
          else: 
            print("Incorrect – la reponse est", mult)
    return reponsesCorrectes
    
reponsesCorrectes = 0
print("Ce logiciel va effectuez un test avec 10 questions …… ");
operation = int(input("SVP choisisser l'operation 0) Addition 1) Multiplication (0 ou 1): "))
      
reponsesCorrectes = effectuezTest(operation)
print(reponsesCorrectes, "reponses correctes.")        
if reponsesCorrectes  <= 6 :
  print("Demandez à votre enseignant(e) pour de l’aide.")
else:
  print("Felicitations!")
