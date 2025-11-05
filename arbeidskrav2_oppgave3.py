"""
Arbeidskrav 2 - Oppgave 3

Cathrine L. Fjeldstad (hei@calif.no)
Oppdatert: Tue Oct  7 17:46:15 2025
"""

import numpy as np  # Importerer numpy for å bruke pi

v_grad = float(input("Skriv inn gradtallet: "))  # Brukeren skriver inn grader

v_rad = v_grad*np.pi/180  # Konverterer grader til radianer

print(f"{v_grad} grader tilsvarer {v_rad:.4f} radianer.")  # Skriver ut resultatet til konsoll