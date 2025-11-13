"""
Arbeidskrav 2 - Oppgave 5
Oppdatert: Wed Nov  5 18:25:12 2025
"""
import numpy as np

a = float(input("Verdien av a er? : "))
b = float(input("Verdien av b er? : "))

areal_trekant = (a*b)/2
areal_sirkel = np.pi*((a**2)/2)
areal_figur = areal_trekant + (areal_sirkel/2)
print(f"Figurens areal er: {areal_figur:.3f}")

omkrets_sirkel = np.pi*a
# Mellomregning for å finne ukjent legnde i trekanten, Pytagoras FTW!
hypotenus = np.sqrt(a**2 + b**2)
omkrets_trekant = a+b+hypotenus
# En av sidene i trekanten er også sirkelens diameter
omkrets_figur = omkrets_sirkel/2 + omkrets_trekant-a
print(f"Figurens omkrets er: {omkrets_figur:.3f}")
