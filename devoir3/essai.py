def elimine_paires(l):
    import random
    resultat=[]
    trash1=[]
    trash2=[]
    PremierLettre=[]
    LettreTriple=[]
    m = l.copy()
    for a in range (0, len(m)):
        for b in range (0,len(m)):
            if b != a :
                if (m[a] != 'J\u2660') and (m[b] != 'J\u2660'):
                    if (m[a])[0] == (m[b])[0]:
                            trash1.append(a)
    print ("trash1 est",trash1)    
    for c in list(set(trash1)):
        trash2.append(m[c])
    for d in trash2 :
        PremierLettre.append(d[0])
    for lettre in PremierLettre :
        if PremierLettre.count(lettre) == 3 :
            LettreTriple.append(lettre)
    for lettretriple in list(set(LettreTriple)):
            trash2.remove(trash2[PremierLettre.index(lettretriple)])
            #trash2.remove(trash2[PremierLettre.find(lettretriple)])
    for e in trash2:
        m.remove(e)
        
                        
    resultat = m
 
    

    random.shuffle(resultat)
    return resultat


