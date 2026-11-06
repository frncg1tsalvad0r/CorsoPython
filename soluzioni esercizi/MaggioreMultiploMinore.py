#Scrivere il programma in Python che legge due numeri senza  virgola da tastiera e stampa se il numero
#più grande è multiplo del più piccolo)
a = int(input("Primo numero"))
b = int(input("Secondo numero"))
if a >= b:
    #Il più grande è a
    if a % b == 0:
        print("Multiplo")
    else:
        print("NON multiplo")
else:
    #Il più grande è b
    if b % a == 0:
        print("Multiplo")
    else:
        print("NON multiplo")
