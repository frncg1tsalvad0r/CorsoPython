import matplotlib.pyplot as plt

f = open('dati.csv', mode='r')
testo = f.read()
f.close()

righe = testo.split("\n")

xs = []
ys = []

for riga in righe:
    colonne = riga.split(";")
    xs.append(int(colonne[0]))
    ys.append(int(colonne[1]))

plt.title("Dati casuali")
plt.grid()
plt.axhline(3)
plt.plot(xs,ys, marker = "o", label = "serie 1", color = "red", linestyle = ":", linewidth=1)
plt.legend(plt.show())

print(xs)
print(ys)
