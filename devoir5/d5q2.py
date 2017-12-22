def etoiles(n1,n):
        '''Precondition pour utiliser la fonction: n1 et n doivent etre egaux et doivent etre des entiers positifs '''
        if n1 > 0:
                if n > 0 :
                    s=''
                    for i in range(n):
                        s += '*'
                    print(s)
                    return(etoiles(n1,n-1))
                
                if n == 0 :
                    return (etoiles(n1,-1))
                
                if -n == n1:
                        s=''
                        for i in range(n1):
                                s += '*'
                        return(print(s))
                        
                if n < 0 :
                        s=''
                        for i in range(-n):
                                s += '*'
                        print(s)
                        return(etoiles(n1,n-1))
        else:
                print("Veuiller inserer un nombre positif")


def sommeListePos_Rec(l,b):
        if b > 0 :
                if l[b-1] > 0:
                        return(l[b-1] + sommeListePos_Rec(l, b-1))
                if l[b-1] < 0:
                        return(sommeListePos_Rec(l, b-1))
        else:
                return(0)
        
        

    
            
            
        
