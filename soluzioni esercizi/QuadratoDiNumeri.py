'''
Scrivere un programma che, dato un numero intero N positivo,
stampa un quadrato di numeri fatto di N righe con i numeri da N a 1 . (2 PUNTI)

ESEMPIO se N = 5 sarà stampato

5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
'''
N = int(input("Inserisci un valore N "))

for _ in range(0, N):
    for c in range(N, 0, -1):
        print(c, " ", end="")
    print()
