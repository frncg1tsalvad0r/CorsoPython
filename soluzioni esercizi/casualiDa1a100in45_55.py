'''
Si vuole scrivere un programma che genera N numeri casuali da 1 a 100 dove
N è un intero inserito dall’utente che è maggiore di zero. 
Scrivere il programma che conta i numeri casuali che cadono nell’intervallo
45-55 (inclusi). (2 PUNTI)
'''
import random
N=int(input("inserisci un numero"))
i=0
conta=0
while i<N:
    casuale=random.randrange(1,101)
    if casuale>=45 and casuale<=55:
        conta+=1
    i+=1
print(conta)
        
        
    
