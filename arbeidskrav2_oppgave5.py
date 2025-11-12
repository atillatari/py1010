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
print("Figurens areal er: ", areal_figur)

omkrets_sirkel = np.pi*a
hypotenus = np.sqrt(a**2 + b**2)
omkrets_trekant = a+b+hypotenus
omkrets_figur = omkrets_sirkel/2 + omkrets_trekant-a
print("Figurens omkrets er:", omkrets_figur)
