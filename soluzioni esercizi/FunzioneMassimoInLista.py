'''
FunzioneMassimoInLista
Scrivere una funzione che calcola il massimo di valori
numerici in una lista
'''


def massimo(lista) :
    '''
    funzione che restituisce il massimo dei valori
    all'interno di una lista
    '''
    max = lista[0]
    for i in range(0, len(lista)):
        if lista[i] > max:
            max = lista[i]

    return max


            
import random

l = []
for i in range(0, 10):
    l.append(random.randrange(0, 100))

print(l)


r = massimo(l)


print("IL massimo è ", r)

    
