'''
Crea un programma che legge le righe di un file CSV, chiamato voti.csv, aventi la seguente stuttura:
Nome, Matematica, Italiano, Scienze, esempio:
Luca,7,8,6
Anna,9,7,8
Scrivi un programma che:
1. legge il file CSV e carica i dati in una lista di dizionari: [{Luca,7,8,6}, {Anna,9,7,8},...];
2. per ogni studente calcola la media dei voti e la stampa;
3. crea un nuovo file CSV, report.csv, avente il seguente formato: Nome|Media, esempio: Luca|7.0.
'''
# 1. Legge voti.csv e carica i dati in una lista di dizionari
file = open("voti.csv", "r")
studenti = []
for riga in file:
    riga = riga.strip()
    if riga != "":
        parti = riga.split(",")
        studente = {
            "nome": parti[0],
            "matematica": int(parti[1]),
            "italiano": int(parti[2]),
            "scienze": int(parti[3])
        }
        studenti.append(studente)
file.close()

# 2. Calcola e stampa la media per ogni studente
file_report = open("report.csv", "w")
for s in studenti:
    media = (s["matematica"] + s["italiano"] + s["scienze"]) / 3
    media = round(media, 1)
    print(s["nome"], "-> media:", media)
    file_report.write(s["nome"] + "|" + str(media) + "\n")
file_report.close()

print("File report.csv creato.")
