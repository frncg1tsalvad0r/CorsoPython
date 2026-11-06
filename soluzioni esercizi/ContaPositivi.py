'''
scrivere una funzione che, dato un array,
restituisce il conteggio dei valori positivi
presenti nell'array
'''
import random
def conta_positivi(lista):
    conta_positivi=0
    lunghezza_lista=len(lista)
    for i in range(0,lunghezza_lista):
        if lista[i]>=0:
            conta_positivi+=1

    return conta_positivi

lista=[]
l=int(input("inserisci la lunghezza della lista"))
for i in range (0,l):
    n_casuale=random.randrange (-100,100)
    lista.append(n_casuale)
print(lista)
print(conta_positivi(lista))

      





            
        
