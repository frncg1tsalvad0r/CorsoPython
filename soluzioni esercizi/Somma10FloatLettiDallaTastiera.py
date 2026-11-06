#Scrivere un programma che chiede all'utente di inserire 10 numeri
# di tipo float e ne fa la somma stampandola a video
# Somma10FloatLettiDallaTastiera

i = 0
somma = 0
while i < 10:
    dato = float(input('Inserisci il dato '));
    somma = somma + dato;
    i += 1

print("La somma è: " + str(somma))