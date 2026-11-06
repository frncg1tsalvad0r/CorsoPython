'''
ESERCIZIO FunzioneMediaAritmetica
Scrivere una funzione che, dato un array di valori reali, restituisca la media aritmetica dei valori (ovvero la somma di tutti i valori diviso il numero di valori)
'''
def media_aritmetica(lista):
    somma = 0
    for i in range (0, len(lista)):
        somma += lista[i]
    
    media = somma / len(lista)
    return media


import random
N = int(input("Inserisci la dimensione della lista: "))

array = []
for i in range (0, N):
    casuale = random.randrange(0, 100)
    array.append(casuale)

print("Array Originale")
print(array)

m = media_aritmetica(array)
print(f"Media dei valori nell'array: {m}")
