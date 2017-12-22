def ajoute1():
    L=[]
    x = str(input("Veuillez rentrer une liste ou une matrice:\n"))
    stopword = ''     
    '\n'.join(iter(input, stopword))

    for element in x.readline() :
        L.append(list(map(int,element.split(' '))))
    
    #x= list(map(int, x.split(' ')))

    #L.append(x.readlines())
    print(L)
    return(L)
        
    '''
    print(L)
    #while input =! '' :
        #L.append(list(map(int,line.strip(' '))))
    stopword = ""
        while True:
            line = input
            if line.strip() == stopword:
                break
            L.append(list(map(int,line.strip(' ')))) '''
    

def essai():
    m= (input(" liste de nombres"))
    x = list(map(int,m.split(' ')))
    print(x)
    return(x)

def essai2(L):
    for i in L:
        i1 = i + 1
        i == i1
    print (L)
    return (L)
