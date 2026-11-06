'''
Scrivere una funzione che, dato un numero intero N positivo,
stampa un triangolo di asterischi di altezza N. 
Scrivere il programma per verificare il corretto
funzionamento della funzione. (1.5 PUNTI)
'''

def triangolo(n):
    for i in range(0, n):
        for j in range(0,i):
            print('*', end='')
        print()

triangolo(8)
