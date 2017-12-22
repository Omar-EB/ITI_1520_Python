# affichez les entier a, a+1, a+2, ..., b
def affiche(a,b):
  for i in range(a, b+1):
    print(i)
    

a = int(input("SVP donner la valeur de a: "))
b = int(input("SVP donner la valeur de b: "))
affiche(a,b)
