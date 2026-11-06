import matplotlib.pyplot as plt
import math

def f(x):
    return math.sin(x) - x 


xs = []
for i in range(-5, 5):
    xs.append(i*0.01)

ys = []
for x in xs :
    ys.append(f(x))

plt.grid()
plt.plot(xs, ys)
plt.show()
