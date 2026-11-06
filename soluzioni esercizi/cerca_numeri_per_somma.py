'''
Creare un programma che assegna ad un array di 20 elementi dei valori casuali (random) minori di 100, quindi,
stampa “TROVATO” se e solo se esistono due elementi nell’array la cui somma sia esattamente uguale a 17.
'''

# Importo la libreria random
import random

# Definisco "a" come una lista vuota, quindi non viene subito alloca la memoria necessaria
a = []
LUN = 20
MAX_RANDOM = 10
SOMMA = 17

for i in range(LUN):
    a.append(random.randint(0,MAX_RANDOM))

print(a)

trovati = False
# Con un doppio ciclo for esamino tutte le possibili coppie
for i in range(LUN):
    # Il ciclo interno lo faccio partire dall'elemento successivo a quello di indice i,
    # altrimenti ogni coppi verrebbe considerata due volte
    for j in range(i+1,LUN):
        if a[i] + a[j] == SOMMA:
            trovati = True
            print(f"I numeri {a[i]} e {a[j]} danno somma {a[i] + a[j]}")
        
if trovati == False:
    print(f"Nessuna coppia di numeri da per somma {SOMMA}")
 
