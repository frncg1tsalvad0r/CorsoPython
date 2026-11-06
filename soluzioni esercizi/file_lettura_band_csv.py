'''
Il programma legge da un file in formato CSV (Comma Separeted Value) un elenco di album prodotti da diverse
band rock (nome, data, titolo album), quindi, legge in input un tervallo di anni e vusualizza in output
gli album prodotti in tale intervallo (estremi inclusi)
'''
f = open("band_rock.csv" , "rt")
a1 = int(input("Anno iniziale (1950-2026) "))
while a1 < 1950 or a1 > 2026:
    a1 = int(input("Anno iniziale (1950-2026) "))
    
a2 = int(input("Anno finale (1950-2026) "))
while a2 < a1 or a2 > 2026:
    a2 = int(input("Anno finale (1950-2026) "))
    
print("\nAlbun stampati nel periodo indicato:\n")
for riga in f:
    #print(riga.strip())
    #print(riga.strip().split(","))
    lista = riga.strip().split(",")
    if int(lista[1])>=a1 and int(lista[1]) <= a2:
        print(riga.strip())
        
f.close()
