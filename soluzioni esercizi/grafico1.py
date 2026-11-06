from matplotlib import pyplot as plt
import math

def f(x):
    return math.sin(x)-0.25*x

xs =[]
for i in range(-500,500):
    xs.append(i*0.01)

ys = []
for x in xs:
    ys.append(f(x))
plt.grid()
plt.title('Grafici')
plt.suptitle('Seno')
plt.plot(xs, ys)
plt.show()
