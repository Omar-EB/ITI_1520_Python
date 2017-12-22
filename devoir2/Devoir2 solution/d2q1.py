def bmi(p, t):
  return p /(t**2)

p = float(input("SVP entre votre poid en kilogrammes "))
t = float(input("SVP entre votre taille en metres "))

r = bmi(p,t)
print("Votre IMC est", r)

if r < 18.5:
    print("Maigreur")
elif r < 25:
    print("Poids ideal")
elif r < 30:
    print("Surpoids")
else:
    print("Obesite")
