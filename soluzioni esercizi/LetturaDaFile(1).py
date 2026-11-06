#Apro un file in lettura
#Leggo e stampo  i dati del file
#sullo schermo
f = open('miofile.txt', 'r')
testo = f.read()
print(testo)
f.close()
