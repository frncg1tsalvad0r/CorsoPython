'''
Scrivere una funzione che, dato una lista di valori numerici interi positivi
restituisca la somma dei numeri pari
'''

def somma_pari(lista):
    somma = 0
    for i in range(0, len(lista)):
        if lista[i] % 2 == 0:
            somma += lista[i]
    return somma

import random
valori = []
for i in range (0, 10):
    casuale = random.randrange(0, 100)
    valori.append(casuale)

print(valori)
print(somma_pari(valori))