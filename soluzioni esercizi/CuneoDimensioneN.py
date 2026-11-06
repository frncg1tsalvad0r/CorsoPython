'''
Scrivere un programma che, dato un intero N positivo,
stampa una figura a forma di cuneo di altezza N+1 asterischi (2 PUNTI)

Ad esempio se N = 3 a schermo verrà stampato

*
 *
  *
****
'''
N=int(input("Altezza"))

for riga in range(0, N):
    # stampo gli spazi
    for spazi in range(0, riga):
        print(" ", end="")
    # stampo l'asterisco e vado a capo
    print("*")
print("*"*(N+1))
