''' aprire file di testo dove si trovano delle parole separate da spazi e conteggiare il numero di parole
stampando un prospetto sulla frequenza es. cane: 2, topo: 5'''
f=open ("conteggio_parole.txt",'r')
testo =f.read()
f.close()
parole = testo.split()
frequenze={}

for parola in parole:
    if parola in frequenze:
        frequenze[parola]+=1
    else:
        frequenze[parola]=1
for parola in frequenze:
    print(parola,frequenze[parola])





