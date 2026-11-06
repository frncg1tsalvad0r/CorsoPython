'''
Scrivi un programma che legga un file di testo chiamato testo.txt (crealo tu con qualche frase di prova)
e conti quante volte appare ogni parola. Salva il risultato in un file chiamato conteggio.txt nel formato:
Parola:N
'''
file = open("testo2.txt", "r")
conteggio = {}
for riga in file:
    for parola in riga.split():
        parola = parola.lower()        # uniforma maiuscole/minuscole
        if parola in conteggio:
            conteggio[parola] = conteggio[parola] + 1
        else:
            conteggio[parola] = 1
file.close()

file_output = open("conteggio.txt", "w")
for parola in conteggio:
    file_output.write(parola + ":" + str(conteggio[parola]) + "\n")
file_output.close()

print("File conteggio.txt creato.")
