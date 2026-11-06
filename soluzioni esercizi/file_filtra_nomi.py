'''
Scrivi un programma che legge i nomi contenuti nel file nomi.txt e crei un nuovo file
chiamato nomi_filtrati.txt contenente solo i nomi che hanno più
di 4 caratteri (esclusi spazi iniziali/finali).
'''

file_input = open("nomi.txt", "r")
file_output = open("nomi_filtrati.txt", "w")

for riga in file_input:
    nome = riga.strip()          # rimuove spazi iniziali/finali e \n
    if len(nome) > 4:
        file_output.write(nome + "\n")

file_input.close()
file_output.close()

print("File nomi_filtrati.txt creato.")
