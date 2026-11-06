#Un gioco consiste nell’indovinare un valore intero
#che si trova in un intervallo di valori tra due interi positivi
#generati dal calcolatore (max 100). Scrivere il programma in Python.
import random
piccolo = random.randrange(0, 100+1)
grande = random.randrange(piccolo, 101)
numero = int(input("Inserisci il numero"))
if numero >= piccolo and numero <= grande:
    print("Hai vinto")
