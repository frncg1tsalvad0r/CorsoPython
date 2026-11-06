'''
Scrivere un programma che chiede all’utente di inserire un numero N di valori.
Il programma verifica se tra gli N valori letti ve ne sono almeno due dispari
(2 PUNTI)

Esempio se l’utente decide di inserire 6 numeri (ovvero N = 6) e i valori
inseriti sono

4 3 2 8 12 18

Il programma stamperà a schermo “NON ci sono due numeri dispari” perché
l’unico dispari è 3.

Esempio se l’utente decide di inserire 5 numeri (ovvero N = 5) e
i valori inseriti sono

2 5 6 12 3 

Il programma stamperà a schermo “Ci sono almeno due numeri dispari”
perchè 5 e 3 sono dispari
'''
N  =int(input("Inserisci un N "))
conta_dispari=0
for i in range(0, N):
    valore = int(input("Inserisci il dato"))
    if valore % 2 == 1:
        conta_dispari+=1

if conta_dispari >= 2:
    print("Ci sono almeno due numeri dispari")
else:
    print("NON ci sono almeno due numeri dispari")
    
