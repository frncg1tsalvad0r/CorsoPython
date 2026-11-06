'''
Scrivere una funzione che ordina una lista di valori numerici in ordine 
crescente usando la strategia del selection sort
'''

def selection_sort(lista):
    '''
    Selection sort. La lista passata come parametro viene ordinata
    '''
    for k in range(0, len(lista)):
        min = lista[k]
        pos_min = k
        for i in range(k, len(lista)):
            if lista[i] < min:
                min = lista[i]
                pos_min = i
        
        # inserisco il minimo nella posizione corretta
        tmp = lista[pos_min]
        lista[pos_min] = lista[k]
        lista[k] = tmp
    
    return

import random
valori = []
for i in range (0, 10):
    casuale = random.randrange(0, 100)
    valori.append(casuale)


print(valori)
selection_sort(valori)
print(valori)