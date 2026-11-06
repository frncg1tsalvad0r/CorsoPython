#Scrivere un programma che, dato il prezzo di un prodotto e lo sconto 
# percentuale ne calcoli il prezzo finale. 
prezzo = float(input("Inserisci il prezzo del prodotto"))
sconto_percentuale = float(input("Inserisci lo sconto percentuale"))
prezzo_finale = prezzo - prezzo*sconto_percentuale/100
print ("Il prezzo scontato vale: " + str(prezzo_finale))