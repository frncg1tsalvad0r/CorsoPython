'''
Creare un programma che popola una lista con 20 numeri casuali e che stampi tutte le
possibili coppie che si possono creare con gli elementi della lista.
'''
import random
N = 20
MAX_RANDOM = 100

# Funzione che riceve come parametri la lunghezza, n, della lista da
# popolare con numeri casuali con valore massimo: max.
def popola_random(n, max):
    a = []
    for i in range(n):
        a.append(random.randint(0,max))
    return a

    
l = popola_random(N, MAX_RANDOM)
print(l)

for i in range(N):
    for j in range(i+1,N):
        print(f"({l[i]},{l[j]})", end = ' ')


