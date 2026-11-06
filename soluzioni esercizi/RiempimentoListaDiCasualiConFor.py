'''
Scrivere un programma che, dato una lista di dimensione 10 elementi, riempia tale lista 
con dei numeri generati casualmente 
(usare la libreria random e costrutto ciclico for).
'''
import random
lista = [0] * 10

for i in range(0, 10):
    lista[i] = random.randint(1, 100)

print(lista)