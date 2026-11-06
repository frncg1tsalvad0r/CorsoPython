'''
scrivere un programma che popola un array di dimensione N
definita dall'utente con valori casuali
Successivamente estrare dall'array il valore minimo e il
valore massimo e stamparli a schermo
'''
import random
N = int (input("inserisci il numero di valori "))
lista = []
for i in range(0,N):
    casuale = random.randrange(1,101)
    lista.append(casuale)

print(lista)

minimo = lista[0]
massimo = lista[0]
for i in range(0,N):
    if lista[i] < minimo:
        minimo = lista[i]
    
    if lista[i] > massimo:
        massimo = lista[i]

print("il valore minimo è " + str(minimo))
print("Il valore massimo è ", massimo)


