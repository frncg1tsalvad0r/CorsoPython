# Far generare dal calcolatore un numero casuale M righe e N colonne da 1 e 3 (inclusi)
# Disegnare un rettangolo di asterischi di M righe e N colonne
# Esempio: se il numeri casuali generati sono M=2 e N=3
# Verrà stampato
# ***
# ***

# Esempio: se il numeri casuali generati sono M=2 e N=2
# Verrà stampato
# **
# **
import random
M = random.randrange(1,4)
N = random.randrange(1,4)

if M == 1 and N == 1:
    print("*")

if M == 2 and N == 1:
    print("*")
    print("*")
    
if M == 3 and N == 1:
    print("*")
    print("*")
    print("*")
    
if M == 1 and N == 2:
    print("**")
    
if M == 2 and N == 2:
    print("**")
    print("**")

if M == 3 and N == 2:
    print("**")
    print("**")
    print("**")

if M == 1 and N == 3:
    print("***")

if M == 2 and N == 3:
    print("***")
    print("***")

if M == 3 and N == 3:
    print("***")
    print("***")
    print("***")
