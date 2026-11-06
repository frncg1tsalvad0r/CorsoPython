import matplotlib.pyplot as plt
import math 

xs = []
for i in range(-100,100):
    xs.append(i*0.01)

def espo(x):
    return math.exp(x)

def loga(x):
    return math.log(x)

y1s = []
for x in xs:
    y1s.append(espo(x))

xs_pos = []
for i in range(1,400):
    xs_pos.append(i*0.01)
    
y2s = []
for x in xs_pos:
    y2s.append(loga(x))

plt.grid()
plt.plot(xs, y1s, label="esponenziale", linewidth="0.5")
plt.plot(xs_pos, y2s, label="logaritmo  ", linewidth="0.5")
plt.legend()
plt.show()

