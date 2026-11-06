'''
Scrivere una funzione che, dato un numero n qualsiasi,
restituisce il valore positivo corrispondente. 
Scrivere il programma per verificare il corretto
funzionamento della funzione. (2 PUNTI)
'''

def assoluto(n):
    if n > 0:
        return n
    return -1*n

print(assoluto(6))
print(assoluto(-6))
