'''
Scrivi un programma che legga un file di testo chiamato "testo.txt"
(crealo tu con qualche frase di prova) e conti quante volte appare
ogni parola. Salva il risultato in un file chiamato "conteggio.txt"
nel formato: parola: N
'''

def conta_parole(nome_file):
    diz = {}
    f = open("testo.txt")
    str = f.read()
    str.strip(".,;\n\r")
    str = str.split()
    for parola in str:
        # Se la parola non esiste la aggiunge (chiave) con valore 0;
        # se la parola esiste incremeta di 1 il valore corrispondente.
        # https://www.w3schools.com/python/python_dictionaries_add.asp
        # https://www.w3schools.com/python/ref_dictionary_get.asp
        diz[parola] = diz.get(parola, 0) +  1
    f.close()
    return diz

f = open("conteggio.txt", "wt")
dizionario = conta_parole("testo.txt")
# Esistono diversi modi di utilizzare il ciclo for con i dizionari. 
# https://www.w3schools.com/python/python_dictionaries_loop.asp
for parola in dizionario:
    f.write(f"{parola}: {dizionario[parola]}\n")
f.close()
print(f"Fatto! {len(dizionario)} parole trovate")
