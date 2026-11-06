# Scrivere un programma che chiede all’utente di inserire 10 numeri interi da tastiera e fa la somma dei soli numeri dispari inseriti
# Se l’utente inserisse 
# 44 21 12 1 30 5 7 33 18 10
# Il risultato stampato dovrà essere 67 ovvero 21+1+5+7+33

i = 0
somma = 0
while i < 10:
    somma = 1
    dato = int(input("Inserire un dato"))
    if dato %2 == 1:    #il numero è dipari
        somma += dato

print(somma)