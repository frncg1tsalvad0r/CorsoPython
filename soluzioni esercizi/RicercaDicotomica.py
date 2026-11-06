import random


def ricerca_dicotomica (l,N):
    inizio=0
    fine=len(l)-1
    while True:
        meta=(fine + inizio)//2
        if N== l[meta]:
            return True
        if N< l[meta]:
            fine= meta-1
        if N> l[meta]:
            inizio=meta +1

        if inizio>fine:
            return False

lista=[]
N=0
for i in range(100000000):
   N= random.randrange(N,N+4)
   lista.append(N)
   
#print(lista)
n=int(input("Inserisci il valore da cercare: "))

print(ricerca_dicotomica(lista,n))

        






            
 
