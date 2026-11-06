'''
Scrivere un programma che, dato un numero intero N positivo,
stampa un quadrato di asterischi e cancelletti N righe ed N colonne alternando,
ad ogni riga, asterischi e cancelletti. (2 PUNTI)

ESEMPIO se N = 5 sarà stampato

*****
#####
*****
#####
*****
'''
N  = int(input("Inserisci N "))
for r in range(0, N):
    if r%2 == 0:
        print("*"*N)
    else:
        print("#"*N)
