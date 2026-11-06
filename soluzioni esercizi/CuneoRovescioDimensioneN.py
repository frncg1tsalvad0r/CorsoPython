'''
Scrivere un programma che, dato un intero N positivo,
stampa una figura a forma di cuneo di altezza N+1 asterischi (2 PUNTI)

Ad esempio se N = 3 a schermo verrà stampato

****
  *
 *
*
'''
N= int(input("Inserisci un numero "))

#prima riga
print("*"*(N+1))
for r in range(0, N):
    print(" "*(N-r-1), end="")
    print("*")

for spazi in range (N-1, 0, -1):
    print(" "*spazi, end=" ")
    print("*")
