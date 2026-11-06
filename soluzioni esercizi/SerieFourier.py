from matplotlib import pyplot as plt
import math

def f(x):
    A = 3
    B = 3
    omega = 1
    alfa = 0.2*math.pi
    return A*math.sin(omega*x + alfa) + B*math.sin(omega*x)

xs = []
for i in range (-1000, 1000):
    xs.append(i*0.01)

ys_serie = []
for x in xs:
    y = math.sin(1*x) + 0.3*math.sin(3*x) 
    ys_serie.append(y)

plt.grid()
plt.axhline()
plt.axvline()
plt.plot(xs, ys_serie, linestyle=':', label="")
plt.legend()
plt.show()
