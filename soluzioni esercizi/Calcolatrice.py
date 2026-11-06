# Scrivere un programma che simula una calcolatrice. 
# Si chiede all’utente di inserire il primo operando, 
# l’operazione tra la + (più), la -(meno), la *(per) e la / (divisione) 
# e infine  il secondo operando.
# Alla fine si stamperà a schermo il risultato dell’operazione, 
# e errore se non è stato selezionato un operatore matematico corretto.

dato1 = float(input("Inserisci il primo operando: "))
operazione = input("+ - * / : ")
dato2 = float(input("Inserisci il secondo operando: "))

if operazione == "+":
    risultato = dato1 + dato2
    print("La somma è :" + str(risultato))
if operazione == "-":
    risultato = dato1 + dato2
    print("La sottrazione è :" + str(risultato))
if operazione == "*":
    risultato = dato1 + dato2
    print("La prodotto è :" + str(risultato))
if operazione == "/":
    risultato = dato1 + dato2
    print("Il rapporto è :" + str(risultato))
