import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt


def f(x):
    return x**3 - 10*x


xs = []
for i in range(-500, 500):
    xs.append(i*0.01)

ys = []
for x in xs :
    ys.append(f(x))

plt.axhline(0, color='black')
plt.axvline(0, linestyle=':')
plt.grid()
plt.plot(xs, ys)
plt.legend([r"$x^3-10\cdot x $"])
plt.show()

