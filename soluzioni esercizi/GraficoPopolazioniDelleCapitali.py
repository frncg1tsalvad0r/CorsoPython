import matplotlib.pyplot as plt

f = open('capitali.csv')
intestazione = f.readline()
righe = f.readlines()
nomi = []
abitanti  = []
for riga in righe:
    riga = riga.strip()
    campi = riga.split(",")
    nomi.append(campi[1])
    abitanti.append(int(campi[3]))

plt.title("Popolazione")
plt.grid()
plt.bar(nomi, abitanti, label="censimento")
plt.legend()
plt.show()