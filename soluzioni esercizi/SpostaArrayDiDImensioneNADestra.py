'''
Scrivere un programma che popola una lista di dimensione N definita dall'utente con valori casuali.
Successivamente mette a zero il massimo e il minimo della lista
'''

import random

N = int(input("Inserisci la dimensione della lista"))

lista = []
for i in range(0,N):
    valore=random.randrange(0, 101)
    lista.append(valore)

print(lista)

for i in range(N-2, -1, -1):
    lista[i+1] = lista[i]

print(lista)
