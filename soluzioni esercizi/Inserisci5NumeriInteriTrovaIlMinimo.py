i = 0
min = int(input("Inserisci un numero intero: "))
while i < 5:
    numero = int(input("Inserisci un numero intero: "))
    if numero < min:
        min = numero
    i += 1
print("Il più piccolo è: " + str(min))