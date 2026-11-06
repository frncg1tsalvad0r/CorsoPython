'''
scrivere un programma che popola un array di dimensione N
definita dall'utente con valori casuali
Successivamente scambia il valore minimo e il valore masssimo
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
pos_minimo = 0
pos_massimo = 0
for i in range(0,N):
    if lista[i] < minimo:
        minimo = lista[i]
        pos_minimo = i
    if lista[i] > massimo:
        massimo = lista[i]
        pos_massimo = i
        

print("il valore minimo è " + str(minimo))
print("Il valore massimo è ", massimo)

''' scambio il minimo con il massimo '''
temp = lista[pos_minimo]
lista[pos_minimo] = lista[pos_massimo]
lista[pos_massimo] = temp

print(lista)
