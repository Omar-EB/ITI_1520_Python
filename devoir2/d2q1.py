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
