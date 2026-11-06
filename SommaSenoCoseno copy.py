import matplotlib.pyplot as plt
import math

xs = []
for i in range(-700,700):
    xs.append(i*0.01)

alfa = 0 
T = 3

def s1(x):
    return math.sin((2*math.pi/T)*x)

def s2(x):
    return math.cos((2*math.pi/T)*x)

A = 1
B = 1
def s3(x):
    return A*s1(x) + A*s2(x)

y1s = []
y2s = []
y3s = []
for x in xs:
    y1s.append(s1(x))
    y2s.append(s2(x))
    y3s.append(s3(x))

plt.grid()
plt.plot(xs, y1s, label="seno", linewidth="0.5")
plt.plot(xs, y2s, label="coseno", linewidth="0.5")
plt.plot(xs, y3s, label="somma", linewidth="2")
plt.legend()
plt.show()

