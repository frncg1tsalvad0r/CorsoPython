'''
ESERCIZIO NumeroPrimo
Scrivere una funzione che, dato un numero naturale
>= 0 restituisca true se il numero è primo, false
altrimenti.
Verificare il funzionamento della funzione con un
programma che legge dalla tastiera un numero naturale
e stampa se è primo oppure no.
'''
N=int(input("inserisci un numero"))

def numero_primo(N):
    for i in range(2, N):
        if N%i==0:
            return False
        
    return True
print(numero_primo(N))
