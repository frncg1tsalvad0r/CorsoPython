minore = int(input("Inserisci un numero intero: "))
maggiore = int(input("Inseriscine un altro maggiore del primo: "))
while minore >= maggiore:
    maggiore = int(input("Questo non è maggiore del primo, inseriscine un altro: "))

print("Il più piccolo è " + str(minore) + ", il più grande è "+ str(maggiore))