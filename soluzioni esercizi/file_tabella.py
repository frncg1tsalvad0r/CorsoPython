'''
Scrivi un programma che legge da un file CSV (Comma Separated Values) dei dati (una tabella)
relativi a misurazioni di laboratorio nel seguente formato:
misura 1|3.5|4.2
quindi, il programma deve calcolare e stampare la media della seconda colonna
'''
f = open("tabella_dati.csv", "rt")
somma = 0
n = 0
for riga in f:
    n = n+1
    print(riga.strip())
    lista = riga.strip().split("|")
    #print(lista)
    somma = somma+float(lista[1])
    #print(float(lista[1]))
    
print(f"media di {n} misurazioni : {somma/n}")
    
    
