'''
Scrivere un programma che chiede all’utente di inserire un numero N di valori.
Il programma verifica se tra gli N valori letti ve ne sono almeno due pari
(2 PUNTI)

Esempio se l’utente decide di inserire 6 numeri (ovvero N = 6) e i valori inseriti sono

1 4 5 3 9 11

Il programma stamperà a schermo “NON ci sono due numeri pari” perchè l’unico pari è 4.

Esempio se l’utente decide di inserire 5 numeri (ovvero N = 5) e i valori inseriti sono

1 4 5 11 2 

Il programma stamperà a schermo “Ci sono almeno due numeri pari”
perchè 4 e 2 sono pari
'''
N=int(input("Inserire il numero di valori"))

conta_pari=0
for i in range(0, N):
    dato  = int (input("Inserisci il valore "))
    if dato % 2 == 0:
        conta_pari +=1

if conta_pari >= 2:
    print("Ci sono almeno due pari")
else:
    print("NON ci sono almeno due pari")
