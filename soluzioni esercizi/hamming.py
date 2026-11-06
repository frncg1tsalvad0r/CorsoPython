'''
Creare un programma che assegna, in modo casuale, a due ad un array di 10 elementi,
i valori 0 o 1, quindi calcola la distanza di Hamming tra i due array.
Distanza di Hamming: è il numero di posizioni in cui due parole di codice (sequenze di bit) differiscono. 
Esempio: La distanza di Hamming tra 1101 e 1011 è 2, perché differiscono nei secondi e terzi bit.
'''

# Importo la libreria random
import random

a = []
b = []
LUN = 10

h = 0

for i in range(LUN):
    a.append(random.randint(0,1))
    b.append(random.randint(0,1))

print(a)
print(b)

for i in range(LUN):
    if a[i] != b[i]:
        h = h+1
print(f"La distanza di Hamming è {h}")


