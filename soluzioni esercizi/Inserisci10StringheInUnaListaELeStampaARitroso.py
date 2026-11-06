
i = 0
lista = [0,0,0,0,0,0,0,0,0,0]
s = input("Inserisci una stringa: ")
while i < 10:  
    lista[i] = s
    i += 1
    s = input("Inserisci una stringa: ")

i = 9
while i >= 0:
    print (lista[i])
    i -= 1 