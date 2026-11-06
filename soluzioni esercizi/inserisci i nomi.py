f = open("nomi.txt", "a")
for i in range (0,5):
    nomi = str(input("inserisci un nome"))
    f.write(nomi)
f.close()
