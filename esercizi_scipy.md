# Esercizi Progressivi in Python con SciPy

Benvenuto in questa raccolta di esercizi progressivi su **SciPy**. Questo documento è strutturato per portarti dai concetti di base dell'algebra lineare fino alla risoluzione di equazioni differenziali e all'interpolazione dei dati, concetti fondamentali nel calcolo scientifico come illustrato in *MatematicaConPython*.

Ogni esercizio presenta un problema e la relativa soluzione in Python. Ti consiglio di leggere la traccia, provare a scrivere il codice sul tuo editor e poi confrontarlo con la soluzione proposta.

---

## Livello 1: Algebra Lineare (`scipy.linalg`)

Il modulo `scipy.linalg` è estremamente ottimizzato per operazioni su matrici, superando le funzioni di base presenti in NumPy.

### Esercizio 1.1: Risolvere un sistema lineare
**Traccia:**
Dato il seguente sistema di equazioni lineari:
$$
\begin{cases}
3x + 2y - z = 1 \\
2x - 2y + 4z = -2 \\
-x + \frac{1}{2}y - z = 0
\end{cases}
$$
Utilizza `scipy.linalg.solve` per trovare i valori di $x$, $y$ e $z$.

**Soluzione:**
```python
import numpy as np
from scipy import linalg

# Definizione della matrice dei coefficienti A e del termine noto b
A = np.array([[3, 2, -1],
              [2, -2, 4],
              [-1, 0.5, -1]])

b = np.array([1, -2, 0])

# Risoluzione del sistema
soluzione = linalg.solve(A, b)

print(f"Soluzione: x={soluzione[0]:.2f}, y={soluzione[1]:.2f}, z={soluzione[2]:.2f}")
```

### Esercizio 1.2: Autovalori e Autovettori
**Traccia:**
Crea una matrice quadrata $M$ di dimensione 3x3 a tua scelta. Calcola gli autovalori e gli autovettori associati utilizzando `scipy.linalg.eig`.

**Soluzione:**
```python
import numpy as np
from scipy import linalg

M = np.array([[1, 2, 3],
              [0, 4, 5],
              [0, 0, 6]])

autovalori, autovettori = linalg.eig(M)

print("Autovalori:\n", autovalori.real)
print("Autovettori:\n", autovettori)
```

---

## Livello 2: Ottimizzazione e Curve Fitting (`scipy.optimize`)

Il modulo `scipy.optimize` permette di trovare minimi, massimi, radici di funzioni e di adattare curve a dati sperimentali.

### Esercizio 2.1: Trovare il minimo di una funzione scalare
**Traccia:**
Definisci la funzione $f(x) = x^2 + 10\sin(x)$. Trova il suo punto di minimo globale (partendo da un'ipotesi iniziale $x_0 = 0$) utilizzando la funzione `minimize`.

**Soluzione:**
```python
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 10 * np.sin(x)

# Ottimizzazione
risultato = minimize(f, x0=0)

print(f"Il minimo si trova in x = {risultato.x[0]:.4f}")
print(f"Valore della funzione al minimo: {risultato.fun:.4f}")
```

### Esercizio 2.2: Adattamento di una curva (Curve Fitting)
**Traccia:**
Genera 50 punti dati rumorosi basati sulla funzione $g(x) = 2.5 \cos(1.5 x) + 0.5$. Utilizza `scipy.optimize.curve_fit` per stimare i parametri originali (ampiezza, frequenza angolare e offset).

**Soluzione:**
```python
import numpy as np
from scipy.optimize import curve_fit

# 1. Definizione della funzione modello
def modello(x, a, w, b):
    return a * np.cos(w * x) + b

# 2. Generazione di dati finti con rumore
x_data = np.linspace(0, 10, 50)
y_vera = modello(x_data, 2.5, 1.5, 0.5)
rumore = 0.5 * np.random.normal(size=x_data.size)
y_data = y_vera + rumore

# 3. Curve fitting
parametri_stimati, covarianza = curve_fit(modello, x_data, y_data)
a_est, w_est, b_est = parametri_stimati

print(f"Parametri stimati: a={a_est:.2f}, w={w_est:.2f}, b={b_est:.2f}")
```

---

## Livello 3: Calcolo Numerico (`scipy.integrate`)

Questo modulo è essenziale per la fisica computazionale e l'analisi numerica.

### Esercizio 3.1: Integrazione definita
**Traccia:**
Calcola l'integrale definito della funzione $h(x) = e^{-x^2}$ nell'intervallo $[0, \infty)$. Usa `scipy.integrate.quad`.

**Soluzione:**
```python
import numpy as np
from scipy.integrate import quad

def h(x):
    return np.exp(-x**2)

# Calcolo dell'integrale da 0 a infinito (np.inf)
valore_integrale, errore_stimato = quad(h, 0, np.inf)

print(f"Valore dell'integrale: {valore_integrale:.6f}")
print(f"Errore stimato: {errore_stimato:.2e}")
```

### Esercizio 3.2: Risolvere un'Equazione Differenziale Ordinaria (ODE)
**Traccia:**
Risolvi l'equazione del decadimento radioattivo $\frac{dy}{dt} = -k y$ con $k = 0.3$ e condizione iniziale $y(0) = 100$. Simula il sistema da $t = 0$ a $t = 15$ usando `scipy.integrate.odeint`.

**Soluzione:**
```python
import numpy as np
from scipy.integrate import odeint

# Definizione del sistema (equazione differenziale)
def decadimento(y, t, k):
    dydt = -k * y
    return dydt

# Condizioni iniziali e tempo
y0 = 100
t = np.linspace(0, 15, 100)
k = 0.3

# Risoluzione
soluzione = odeint(decadimento, y0, t, args=(k,))

print("Primi 5 valori di y:", soluzione[:5].flatten())
```

---

## Livello 4: Statistica (`scipy.stats`)

SciPy fornisce un'enorme libreria per distribuzioni statistiche e test.

### Esercizio 4.1: Distribuzione Normale
**Traccia:**
Istanzia una distribuzione normale con media $\mu = 5$ e deviazione standard $\sigma = 2$.
1. Calcola la probabilità che un valore sia minore o uguale a 7 usando la CDF (Cumulative Distribution Function).
2. Genera 1000 campioni casuali da questa distribuzione e calcola la loro media empirica.

**Soluzione:**
```python
from scipy.stats import norm
import numpy as np

mu = 5
sigma = 2

# Istanzia la distribuzione
distribuzione = norm(loc=mu, scale=sigma)

# 1. Calcolo della CDF per x = 7
prob = distribuzione.cdf(7)
print(f"Probabilità P(X <= 7): {prob:.4f}")

# 2. Generazione campioni e calcolo media
campioni = distribuzione.rvs(size=1000)
media_empirica = np.mean(campioni)
print(f"Media dei campioni (dovrebbe essere vicina a {mu}): {media_empirica:.4f}")
```

---

## Livello 5: Interpolazione di Dati (`scipy.interpolate`)

L'interpolazione è utilissima quando hai punti discreti e vuoi stimare i valori intermedi.

### Esercizio 5.1: Interpolazione Spline 1D
**Traccia:**
Dati 10 punti equispaziati tra 0 e 10 per la funzione $y = \sin(x)$, utilizza `scipy.interpolate.interp1d` per creare una funzione di interpolazione cubica e calcolare i valori su una griglia più fitta di 100 punti.

**Soluzione:**
```python
import numpy as np
from scipy.interpolate import interp1d

# Dati noti (sparsi)
x_conosciuti = np.linspace(0, 10, 10)
y_conosciuti = np.sin(x_conosciuti)

# Creazione della funzione di interpolazione cubica
interpolatore_cubico = interp1d(x_conosciuti, y_conosciuti, kind='cubic')

# Nuova griglia fitta per cui vogliamo stimare y
x_fitti = np.linspace(0, 10, 100)
y_stimati = interpolatore_cubico(x_fitti)

print(f"Valore interpolato in x=1.5: {interpolatore_cubico(1.5):.4f}")
print(f"Valore reale in x=1.5: {np.sin(1.5):.4f}")
```