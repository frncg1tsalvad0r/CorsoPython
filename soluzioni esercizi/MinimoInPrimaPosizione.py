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

minimo = lista[0]
massimo = lista[0]
pos_minimo = 0
pos_massimo = 0

for i in range(0,N):
    if lista[i] < minimo:
        minimo = lista[i]
        pos_minimo = i

    if lista[i] > massimo:
        massimo = lista[i]
        pos_massimo = i
lista[pos_minimo] = 0
lista[pos_massimo] = 0

    
