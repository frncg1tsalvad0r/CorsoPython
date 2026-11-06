f = open('testo.txt', 'r')
testo = f.read()
parole = testo.split(' ')
print(len(parole))
f.close()

f = open('testo.txt', 'r')
righe = f.readlines()
f.close()

print(righe)
lunghezza_riga_max = 0
riga_piu_lunga = ""
for riga in righe:
    if len(riga) >= lunghezza_riga_max:
        lunghezza_riga_max = len(riga)
        riga_piu_lunga = riga

print(riga_piu_lunga)
g = open('riga_lunga.txt', 'w')
g.write(riga_piu_lunga)
g.close()
