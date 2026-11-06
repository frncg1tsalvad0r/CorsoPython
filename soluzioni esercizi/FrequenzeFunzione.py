'''
Scrivere una funzione che, data una lista e un valore
ritorna il numero di volte che tale valore
compare nella lista.
Provarlo con una lista di valori a piacere (lunga
quanto si vuole con valori che a caso)
'''

def frequenze(lista, val):
    c = 0
    for i in range(0, len(lista)):
        if lista[i] == val:
            c+= 1

    return c

import random

l = []
for i in range(0, 20):
    l.append(random.randrange(0, 10))

print(l)

for i in range(0, len(l)):
    print("il valore ", l[i], " compare ", conta_valori(l, l[i]), " volte")

