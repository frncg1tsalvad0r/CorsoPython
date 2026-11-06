'''
Scrivere un programma che, dato un intero N positivo,
stampa una figura a forma di cuneo di altezza N+1 cancelletti (2 PUNTI)

Ad esempio se N = 3 a schermo verrà stampato

#
 #
  #
####
'''
N = int(input("Inserisci un numero intero"))

for r in range (0, N):
    print(" "*r, end="")
    print("#")
print("#"*(N+1))
