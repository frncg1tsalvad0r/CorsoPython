'''
Crea un programma per gestire una rubrica telefonica. I dati sono salvati in un file rubrica.txt, con una
persona per riga nel formato: Nome Cognome;Numero (es: Mario Rossi;333-1234567).
1. leggi il file e carica i dati in un dizionario dove la chiave è il nome e il valore è il numero
2. stampa tutta la rubrica;
3. chiede all’utente di inserire in input un nome ed un numero di telefono, quindi, lo aggiunge al file
'''
# 1. Legge il file e carica i dati in un dizionario
rubrica = {}
file = open("rubrica.txt", "r")
for riga in file:
    riga = riga.strip()
    if riga != "":
        parti = riga.split(";")
        nome = parti[0]
        numero = parti[1]
        rubrica[nome] = numero
file.close()

# 2. Stampa tutta la rubrica
print("=== RUBRICA ===")
for nome in rubrica:
    print(nome, "->", rubrica[nome])

# 3. Aggiunge un nuovo contatto
nuovo_nome = input("Inserisci nome e cognome: ")
nuovo_numero = input("Inserisci numero di telefono: ")

rubrica[nuovo_nome] = nuovo_numero

file = open("rubrica.txt", "a")   # "a" = append, non cancella il contenuto
file.write(nuovo_nome + ";" + nuovo_numero + "\n")
file.close()

print("Contatto aggiunto.")
