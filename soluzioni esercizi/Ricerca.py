import random
lista=[]
N=0
for i in range(100000000):
   N= random.randrange(N,N+4)
   lista.append(N)
   

def ricerca (l,N):
    '''ritorna True se il dato è nella lista
        false se non lo è '''
    a=False
    for i in range(len(l)):
        if l[i]==N:
            a=True
    
    return a
            
#print(lista)       
n=int(input("Inserisci il dato da cercare: "))       

print(ricerca (lista,n))

    
