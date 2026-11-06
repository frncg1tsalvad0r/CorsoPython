#scrivere un programma in Python
#che, dato un numero naturale positivo N
#disegna un triangolo di astetrischi della forma seguente

#Se N = 3

#*
#**
#***

N = int(input("inserisci N"))

i = 1
while i <= N:
    #sfrutto il ciclo per stampare le righe

    j = 1
    while j <= i:
        print("*", end="")

        j+=1


    print("")
    i+=1
