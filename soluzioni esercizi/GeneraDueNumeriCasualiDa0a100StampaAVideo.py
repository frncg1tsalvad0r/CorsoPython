import random
min = random.randrange(0, 101)
max = random.randrange(min, 101)
print("Il minimo generato è :" + str(min) + "e il massimo è: " + str(max))
i = min
while i <= max:
    print (i)
    i += 1