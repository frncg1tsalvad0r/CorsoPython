""" 
Scrivere un programma che, dopo aver letto un numero intero N da tastiera, 
riempie una lista di N numeri casuali.
Successivamente al riempimento della lista, estrarre dalla lista il numero 
più piccolo e stamparlo a schermo (per la ricerca del numero minimo usare un ciclo for)
"""
import random
N = int(input("Inserisci un numero intero positivo: "))

lista = []
for i in range(N):
    casuale = random.randint(1, 100)
    lista[i] = casuale

print(lista)

minimo = lista[0]
for i in range(1, N):
    if lista[i] < minimo:
        minimo = lista[i]

print("Il numero minimo è:", minimo)