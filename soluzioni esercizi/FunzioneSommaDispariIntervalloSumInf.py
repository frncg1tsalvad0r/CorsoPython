'''
ESERCIZIO FunzioneSommaDispariIntervalloSumInf
Scrivere una funzione che calcoli la somma di tutti i
valori  dispari compresi nell’intervallo [x;y] con
x < y

'''


def somma_dispari(inf, sup):
    somma = 0
    for i in range(inf, sup + 1):
        if i % 2 != 0:
            somma += i
    return somma

x = int(input("Inserisci un numero intero "))
y = int(input("Inserisci un numero intero "))

print(f"La somma di tutti i  dispari tra {x} e {y} è ", somma_dispari(x, y))
