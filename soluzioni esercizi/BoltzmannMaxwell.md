Per ricavare la distribuzione delle velocità di Maxwell-Boltzmann, partiamo dalla legge di distribuzione delle energie di Boltzmann e applichiamo considerazioni geometriche nello "spazio delle velocità".
Ecco i passaggi logici e matematici per la derivazione.
------------------------------
## 1. La densità di probabilità nello spazio tridimensionale
Secondo la statistica di Boltzmann, la probabilità che una molecola di gas perfetto (di massa $m$ a temperatura assoluta $T$) abbia una componente della velocità lungo un asse (ad esempio $v_x$) è proporzionale al fattore di Boltzmann dell'energia cinetica associata:
$$P(v_x) = A \cdot e^{-\frac{\frac{1}{2}mv_x^2}{k_B T}} = A \cdot e^{-\frac{mv_x^2}{2k_B T}}$$ 
Poiché il movimento nello spazio è isotropo (uguale in tutte le direzioni) e le componenti $v_x, v_y, v_z$ sono statisticamente indipendenti, la probabilità congiunta di avere una molecola con velocità contemporanee $(v_x, v_y, v_z)$ è il prodotto delle singole probabilità:
$$P(v_x, v_y, v_z) = P(v_x)P(v_y)P(v_z) = A^3 \cdot e^{-\frac{m(v_x^2 + v_y^2 + v_z^2)}{2k_B T}}$$ 
Ricordando che il modulo quadro della velocità totale è $v^2 = v_x^2 + v_y^2 + v_z^2$, la funzione diventa:
$$P(v_x, v_y, v_z) = A^3 \cdot e^{-\frac{mv^2}{2k_B T}}$$ 
## 2. Normalizzazione della costante $A$
Per trovare la costante di proporzionalità $A$, imponiamo che la probabilità totale nello spazio delle velocità sia pari a 1 (condizione di normalizzazione):
$$\int_{-\infty}^{+\infty} A \cdot e^{-\frac{mv_x^2}{2k_B T}} dv_x = 1$$ 
Questo è un classico integrale gaussiano del tipo $\int_{-\infty}^{+\infty} e^{-ax^2} dx = \sqrt{\frac{\pi}{a}}$, dove $a = \frac{m}{2k_B T}$. Risolvendo l'integrale otteniamo:
$$A \cdot \sqrt{\frac{2\pi k_B T}{m}} = 1 \implies A = \left(\frac{m}{2\pi k_B T}\right)^{1/2}$$ 
Di conseguenza, la costante tridimensionale $A^3$ sarà:
$$A^3 = \left(\frac{m}{2\pi k_B T}\right)^{3/2}$$ 
## 3. Passaggio al modulo della velocità (Guscio Sferico)
A noi non interessa la direzione del vettore velocità, ma solo il suo modulo (il "valore" numerico $v$).
Nello spazio tridimensionale delle velocità $(v_x, v_y, v_z)$, l'insieme dei punti che hanno lo stesso modulo $v$ si trova sulla superficie di una sfera di raggio $v$. Se vogliamo calcolare la probabilità che il modulo sia compreso tra $v$ e $v + dv$, dobbiamo considerare il volume di un guscio sferico infinitesimo di spessore $dv$.
Il volume di questo guscio è la superficie della sfera per il suo spessore:
$$dV_v = 4\pi v^2 dv$$ 
Moltiplichiamo quindi la densità di probabilità spaziale per il volume del guscio sferico.
## 4. La funzione di distribuzione finale
Unendo la costante normalizzata e l'elemento di volume geometrico, otteniamo la funzione di distribuzione di Maxwell-Boltzmann $f(v)$:
$$f(v) dv = 4\pi v^2 \left(\frac{m}{2\pi k_B T}\right)^{3/2} e^{-\frac{mv^2}{2k_B T}} dv$$ 
La funzione esprime la frazione di particelle che possiedono una velocità compresa tra $v$ e $v+dv$.
------------------------------
## Rappresentazione Grafica della Funzione
La curva non è una normale gaussiana simmetrica a causa del termine quadratico $4\pi v^2$, che la schiaccia verso lo zero per velocità molto basse e crea un'asimmetria con una "coda" verso le alte velocità.
Nel grafico si distinguono tre velocità caratteristiche fondamentali:

   1. Velocità più probabile ($v_{mp}$): Corrisponde al massimo della curva, ricavabile ponendo la derivata prima della funzione uguale a zero: $\sqrt{\frac{2k_BT}{m}}$.
   2. Velocità media ($\langle v \rangle$): La media aritmetica delle velocità: $\sqrt{\frac{8k_BT}{\pi m}}$.
   3. Velocità quadratica media ($v_{rms}$): Legata all'energia cinetica media del sistema: $\sqrt{\frac{3k_BT}{m}}$.

Desideri vedere la derivazione matematica passo-passo per calcolare una di queste velocità caratteristiche (come la velocità più probabile tramite derivata)? Oppure ti interessa l'applicazione di questa formula in un esercizio pratico?

