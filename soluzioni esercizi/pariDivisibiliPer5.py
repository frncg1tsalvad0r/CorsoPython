'''
Un utente vuole calcolare la somma di tutti gli interi positivi pari
e divisibili per 5 nell'intervallo da 1 a  N dove N è un valore inserito
dallo stesso utente. Scrivere il codice che computa tale problema. (2 PUNTI
'''

N=int(input("inserisci un numero"))
i=0
somma=0
while i<N:
    if i%2==0 and i%5==0:
        somma=somma+i
    i+=1
print(somma) 
