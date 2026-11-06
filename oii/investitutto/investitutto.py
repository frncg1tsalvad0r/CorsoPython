#!/usr/bin/env python3
# NOTA: si raccomanda di usare questo template anche se non lo si capisce completamente.

import sys

# decommenta le due righe seguenti se vuoi leggere/scrivere da file
sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')

T = int(input().strip())
for test in range(1, T+1):
    input()
    N = int(input().strip())

    V = list(map(int, input().strip().split()))

    G = list(map(int, input().strip().split()))

    ris = V[0]+G[0]*N
    # INSERISCI IL TUO CODICE QUI
    for i in range(1, N):
        tot = V[i]+G[i]*(N-i)
        if tot >= ris:
            ris = tot
            
    print("Case #%d: " % test, end='')
    print(ris)

sys.stdout.close()
