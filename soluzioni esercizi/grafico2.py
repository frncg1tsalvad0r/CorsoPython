from matplotlib import pyplot as plt
import math

def g(x):
    return x**3-10*x

def f(x):
    return math.sin(x)-0.25*x

xs =[]
for i in range(-500,500):
    xs.append(i*0.01)

ygs = []
for x in xs:
    ygs.append(g(x))

yfs = []
for x in xs:
    yfs.append(f(x))

plt.suptitle('Grafici')
plt.subplot(2,1,1)    

plt.title('Grafico 1')
plt.grid()

plt.plot(xs, yfs)

plt.subplot(2,1,2)    
plt.title('Grafico 2')
plt.grid()
plt.plot(xs, ygs)

plt.subplot(2,3,5)    
plt.title('Grafico 2')
plt.grid()
plt.plot(xs, ygs)

plt.show()

