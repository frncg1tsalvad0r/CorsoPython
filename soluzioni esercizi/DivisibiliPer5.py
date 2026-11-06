'''
Scrivere un programma che, dato un numero intero positivo N inserito
dall’utente, e scriva se è divisibile per 5 oppure no. (2 PUNTI)
'''
N = int (input("Inserisci N "))

if N % 5 == 0:
    print("Multiplo di 5 ")
else:
    print("NON multiplo di 5")
