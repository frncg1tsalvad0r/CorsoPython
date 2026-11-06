# Scrivere un programma in cui il computer genera un numero casuale
# da 1 a 10 e successivamente chiede all'utente di indovinare tale
# numero
import random

casuale = random.randrange(1, 11)
dato = int(input("Ho pensato ad un numero da 1 a 10: indovina quale "))
if dato == casuale:
    print("Hai indovinato")
else:
    print("Hai sbagliato")
    print("Avevo pensato al numero " + str(casuale))
