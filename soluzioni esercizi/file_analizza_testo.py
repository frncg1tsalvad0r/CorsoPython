'''
Scrivi un programma che analizzi le parole contenute in un file di testo chiamato testo.txt.
1. leggi il file e crea una lista con tutte le parole (separate da spazi o a capo); stampa il totale delle
parole lette.
2. conta e stampa il numero totale di righe presenti nel file;
3. scrivi, in un nuovo file, riga_lunga.txt, la riga più lunga trovata nel file originale;
'''
# 1. Legge tutte le parole
file = open("testo2.txt", "r")
parole = []
righe = []
for riga in file:
    righe.append(riga)
    for parola in riga.split():
        parole.append(parola)
file.close()

print("Totale parole:", len(parole))

# 2. Conta le righe
print("Totale righe:", len(righe))

# 3. Trova la riga più lunga e la salva
riga_piu_lunga = ""
for riga in righe:
    if len(riga) > len(riga_piu_lunga):
        riga_piu_lunga = riga

file_output = open("riga_lunga.txt", "w")
file_output.write(riga_piu_lunga)
file_output.close()

print("Riga più lunga salvata in riga_lunga.txt")
