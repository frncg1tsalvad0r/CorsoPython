'''
Scrivere un programma che verifica il funzionamento
della sympy solve per la soluzione delle equazioni 
e sistemi di equazioni generiche
'''
import sympy as sy

s, v, t  = sy.symbols('x v t')

eom = sy.Eq(v, s/t)

#risolvo l'equazione rispetto alla variabile s
#la seguente restituisce la soluzione in formato lista
print(sy.solve(eom, s))

#meglio usare l'opzione dict=True
print(sy.solve(eom, s, dict=True))

#posso usare la più moderna solveset che restituisce sempre lo stesso formato 
# insieme
print(sy.solveset(eom, s))

