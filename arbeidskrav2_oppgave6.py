"""
Arbeidskrav 2 - Oppgave 6
Oppdatert: Wed Nov  5 18:38:16 2025
"""

import numpy as np
import matplotlib.pyplot as plt

# Lager en array med x-verdier jevnt fordelt fra -10 til 10
x = np.linspace(-10, 10, 200)

# Beregner y-verdiene for f(x) = -x^2 - 5
y = -x ** 2 - 5

# Legger til tittel og aksenavn
plt.title("Grafen til f(x) = -x^2 - 5")
plt.xlabel("x")
plt.ylabel("f(x)")

# Plotter grafen
plt.plot(x, y)

# Viser grafen
plt.show()
