'''
Scrivi un programma che:
1. legge in input un numero interoN, compreso tra 1 e 50
2. memorizza, in un file di testo, N righe di asterischi dove la i-esima riga contiene un numero i di
asterischi; esempio, seN=3, il file conterrà:
*
**
***
'''
N = int(input("Inserisci un numero tra 1 e 50: "))

file = open("triangolo.txt", "w")
for i in range(1, N + 1):
    riga = "*" * i
    file.write(riga + "\n")
    print(riga)
file.close()

