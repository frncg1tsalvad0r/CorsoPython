'''ESERCIZIO PiuContiguo
Scrivere una funzione che, data una lista di numeri interi, restituisca
il numero che compare nel gruppo contiguo più numeroso (se ci sono gruppi
con la stessa numerosità ritornerà uno dei gruppi)
ESEMPIO:
Se ho una lista 
[1,3,7,4,9,9,3,5,5,5,8,2]
la funzione ritorna il valore 5 perché 5 appartiene al gruppo contiguo più
numeroso
Verificare il funzionamento della funzione popolando una lista con dei dati
a piacere.'''


def piu_contiguo(lista):
    frequenza_maggiore=1
    valore=lista[0]
    conta=1
    for i in range(1, len(lista)):
        if lista[i]==lista[i-1]:
            conta+=1
            print(lista[i], conta)
        else:
            conta=1
            
        if conta>frequenza_maggiore:
            frequenza_maggiore = conta
            valore=lista[i]

    return (valore, frequenza_maggiore)

import random
l=[]
for i in range(0,20):
    l.append(random.randrange(0,5))
print(l)
print(piu_contiguo(l))

