import matplotlib.pyplot as plt
import math

xs = []
for i in range(-700,700):
    xs.append(i*0.01)

alfa = 0 # math.pi/12
T = 1
dT = 0.1

def s1(x):
    return math.sin(2*math.pi/T*x)

def s2(x):
    return math.sin(2*math.pi/(T+dT)*x + alfa)

def s3(x):
    return s1(x) + s2(x)

y1s = []
y2s = []
y3s = []
for x in xs:
    y1s.append(s1(x))
    y2s.append(s2(x))
    y3s.append(s3(x))

plt.grid()
plt.plot(xs, y1s, label="s1", linewidth="0.5")
plt.plot(xs, y2s, label="s2" , linewidth="0.5")
plt.plot(xs, y3s, label="s3")
plt.legend()
plt.show()

