from matplotlib import pyplot as plt
import math

x = [x for x in range(-360, 361)]  # Degrees from 0 to 360
y = [math.atan(val * math.pi / 180) for val in x]  # Sine values
plt.plot(x, y)
plt.show()
