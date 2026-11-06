import matplotlib.pyplot as plt


def f(x):
    return 3*x**2 + x + 1


xs = []
for i in range(-5, 5):
    xs.append(i*0.01)

ys = []
for x in xs :
    ys.append(f(x))

plt.grid()
plt.plot(xs, ys)
plt.show()
