#!/usr/bin/env python3
# NOTA: si raccomanda di usare questo template anche se non lo si capisce completamente.

import sys

def pos_min(P, C):
    pm = 0
    m = C[0]
    for i in range(len(C)):
        if P[i] == 0:
            break
        
        if C[i]<m:
            m = C[i]
            pm=i

    return pm

# decommenta le due righe seguenti se vuoi leggere/scrivere da file
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input().strip())
for test in range(1, T+1):
    input()
    N = int(input().strip())

    P = list(map(int, input().strip().split()))

    C = list(map(int, input().strip().split()))

    ris = 0

    while True:
        
        if P[0] == 0:
            break

        pm = pos_min(P, C)

        j = pm
        while j < N and P[j] != 0:
            ris = ris + P[j]*C[pm]
            P[j]=0
            j+=1

    # INSERISCI IL TUO CODICE QUI


    print("Case #%d: " % test, end='')
    print(ris)

sys.stdout.close()
