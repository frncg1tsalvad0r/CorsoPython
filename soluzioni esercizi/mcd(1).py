'''
ESERCIZIO MassimoComunDivisoreFunzione
Scrivere il programma MassimoComunDivisore inglobando
in una funzione che restituisce il MCD dati due numeri interi
'''

def MCD(a, b):
    while True:
        resto = a % b
        if resto == 0:
            McD = b
            break;
        a = b
        b = resto

    a = 100
    return McD

        
primo = a = int(input("Inserisci il primo valore "))
secondo = b = int(input("Inserisci il secondo valore "))


#immagino che a sia  > b
r = MCD (a,b)
print (f"Il massimo comun divisore di {primo} e {secondo} è {r}")
print(a)
    
