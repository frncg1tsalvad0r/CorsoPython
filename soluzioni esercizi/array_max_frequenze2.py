'''
Creare un programma che assegna ad un array (lista) di 100 elementi dei
valori casuali (random) minori o uguali a 30, quindi, stampare in output
il valore che nell’array compare il maggior numero di volte.
'''

import random # Importo la libreria

LUN = 15
MAX_RANDOM = 4
a = [] # Definisco a come una lista ma non alloca la memoria necessaria
# Definisco un array per la memorizzazione delle frequenze degli elementi e delle
# loro posizioni

freq = []

for i in range(LUN):
    a.append(random.randint(0,MAX_RANDOM))
    #a[i] = random.randint(0,30) non va bene perchè la memoria non è stata assegnata

print(a)

for i in range(LUN):
    trovato = False
    for k in range(0,len(freq),2):
        if freq[k] == a[i]:
            trovato = True
            
    if trovato == False:
        freq.append(a[i])
        cont = 0
        for j in range(LUN):
            if a[i] == a[j]:
                cont = cont +1
        freq.append(cont)  


print("---")
print(freq)




