'''
ESERCIZIO FunzioneMinimoInLista
Scrivere una funzione che data una lista di valori numerici,
restituisce il minimo.
'''

def minimo(lista):
    '''
    restituisce il minimo della lista passata come parametro
    '''
    lung = len(lista)
    minimo = lista[0]
    for i in range(0, lung):
        if lista[i] < minimo:
            minimo = lista[i]

    return minimo
        



    
import random
print("Sto generando i numeri casuali")

casuali = []
for i in range(0, 10):
    casuali.append(random.randrange(0,100))

print(casuali)
m = minimo(casuali)
print("Il minimo è ", m)


