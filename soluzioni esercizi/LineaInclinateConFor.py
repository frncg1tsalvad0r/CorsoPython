'''
Scrivere un programma che, dato un numero N intero positivo letto da tastiera,  
stampa una linea di asterischi alta N e larga N
'''

N = int(input("Inserisci un numero intero positivo: "))

for i in range(N):
    print(" " * i, end="")
    print("*")