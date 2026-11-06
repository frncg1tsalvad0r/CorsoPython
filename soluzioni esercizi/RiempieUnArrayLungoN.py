'''
Scrivere un programma che popola una lista di dimensione N con valori float inseriti dall’utente
Successivamente stampa la lista
'''
N = int(input("Inserisci un numero N "))

lista = []
for i in range(0, N):
    valore = float(input("Inserisci valore "))
    lista.append(valore)

print(lista)
