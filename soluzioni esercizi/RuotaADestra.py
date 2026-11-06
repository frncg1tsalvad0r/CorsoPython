'''
Scrivere una funzione che, dato un array di valori qualsiasi, sposta tutti gli elementi verso la testa 
(ovvero a sinistra) di un posto inserendo il primo elemento in coda.
ESEMPIO:
Supposto di avere il seguente array di valori
3, 5, 8, 2, 9, 22
dopo la chiamata alla funzione l'array dovrà avere i seguenti valori
5, 8, 2, 9, 22, 3
Il numero 3 che era in testa è stato reinserito in coda.
'''

def ruota_a_destra(lista):
    '''
    Ruota il contenuto dell'array a destra
    '''
    #salvo l'elemento in coda 
    tmp = lista[len(lista)-1]
    for i in range (len(lista)-1, 0, -1):
        lista[i] = lista[i-1]

    #ripristino il valore che si trovava in coda e lo rimetto in testa
    lista[0] = tmp
    return

import random
N = int(input("Inserisci la dimensione della lista: "))

array = []
for i in range (0, N):
    casuale = random.randrange(0, 100)
    array.append(casuale)

print("Array originale")
print(array)
ruota_a_destra(array)
print("Array ruotato a destra")
print(array)
