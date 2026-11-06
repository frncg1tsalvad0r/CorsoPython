#Scrivere il programma in Python che legge due numeri senza
#virgola da tastiera e stampa se il numero più grande è multiplo
#del più piccolo nell’origine.
primo = int(input("Primo"))
secondo = int(input("Secondo"))

if primo >= secondo:
    if primo % secondo == 0:
        print(str(primo) + "Multiplo" + str(secondo))
else:
    if secondo % primo == 0:
        print(str(secondo) + "Multiplo" + str(primo))
