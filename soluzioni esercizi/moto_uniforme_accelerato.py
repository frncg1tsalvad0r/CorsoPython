'''
Creare le funzioni:
- una funzione (spazio) che calcoli lo spazio percorso da un corpo
che si muove di moto uniformemente accelerato: s = v0 t + (a t2) / 2;
i parametri della funzione sono:  v0 , t, a. 
- una funzione (tempo) che riceve come parametri una lista vuota, e
due numeri reali: base, delta, quindi, restituisce la lista popolata
con i 100 valori reali, calcolati nel seguente modo:
base, base+delta, base+2*delta, base+3*delta,..,base+99*delta (la lista rappresenta 100 istanti di tempo “intervallati” dal valore delta)

Creare poi il programma che legge in input i valori della velocità
iniziale (v0) e 	dell’accelerazione (a). Si devono poi creare
due liste (t, s), inizialmente vuote, quindi:
la prima lista (t) dovrà essere popolata mediante la seconda funzione (tempo).
la seconda lista (s) dovrà essere popolata con i valori restituiti dalla
prima funzione (spazio), ognuno, calcolato usando il corrispondente
istante di tempo prelevato dalla prima lista (t). 
'''
import matplotlib.pyplot as plt

def spazio(t,v0=10,a=2):
    if t>=0:
        return v0*t+(a*t^2)/2
    else:
        return "errore"
    
def tempo(tl,base,delta):
    for i in range(100):
        tl.append(base+delta*i)
    return tl

s=[]
tl=[]
print(tempo(t,5,2))

for i in range(100):
    s.append(spazio(tl[i],20,3))

print(s)
    




