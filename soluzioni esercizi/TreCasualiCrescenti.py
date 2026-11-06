# Genera tre numeri casuali crescenti (non strettamente) da 1 a 10.

import random
primo = random.randrange(1, 10)
secondo = random.randrange(primo, 10)
terzo = random.randrange(secondo, 10)
print(primo, secondo, terzo)
