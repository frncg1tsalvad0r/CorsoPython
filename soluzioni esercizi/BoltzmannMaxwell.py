import matplotlib.pyplot as plt
import math

xs = []
for i in range(0, 1000):
    xs.append(i*3)

N=1
u = 1.660539e-27    # Unità di massa atomica (kg)
# Proprietà del gas (Esempio: Elio, He -> ~4 unità di massa atomica)
m = 4.0026 * u 
T = 273
k_B = 1.380649e-23

def maxwell(v):
    """Calcola la densità di probabilità della distribuzione di Maxwell-Boltzmann."""
    corpo = (m / (2 * math.pi * k_B * T))**(1.5)
    esponente = math.exp(- (m * v**2) / (2 * k_B * T))
    return corpo * 4 * math.pi * v**2 * esponente

y1s = []
for x in xs:
    y1s.append(maxwell(x))

plt.grid()
plt.plot(xs, y1s, label="dN/dv", linewidth="0.5")
plt.legend()
plt.show()
