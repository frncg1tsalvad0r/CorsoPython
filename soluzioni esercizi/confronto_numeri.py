nome1 = input("Inserisci il nome della prima persona")
eta1 = int(input("Inserisci eta' della prima persona"))
nome2 = input("Inserisci il nome della seconda persona")
eta2 = int(input("Inserisci eta' della seconda persona"))
if eta1 > eta2:
    print(nome1 + " e' più vecchio di " + nome2)
else:
    print(nome2 + " e' più vecchio di " + nome1)