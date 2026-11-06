'''
Scrivere un programma che chiede all’utente di inserire un numero N di valori.
Il programma verifica se tra gli N valori letti ve ne sono almeno due multipli
di 3 (2 PUNTI)

Esempio se l’utente decide di inserire 6 numeri (ovvero N = 6) e i
valori inseriti sono

1 6 5 2 8 11

Il programma stamperà a schermo “NON ci sono due numeri multipli di 3”
perchè l’unico multiplo di 3 è 6.

Esempio se l’utente decide di inserire 5 numeri (ovvero N = 5) e i
valori inseriti sono

1 9 5 11 12

Il programma stamperà a schermo “Ci sono almeno due numeri multipli di 3” perché 9 e 12 sono multipli di 3
'''
N = int(input("Insderisci N "))
conta_multipli_tre = 0
for i in range (0, N):
    dato = int(input("Inserisci il dato "))
    if dato % 3 == 0:
        conta_multipli_tre+= 1

if conta_multipli_tre >= 2:
    print("Ci sono almeno due valori multipli di 3")
else:
    print("NON ci sono almeno due valori multipli di 3")
