"""
Arbeidskrav 2 - Oppgave 5

Cathrine L. Fjeldstad (hei@calif.no)
Oppdatert: Wed Nov  5 18:25:12 2025
"""
import numpy as np

a = int(input("Verdien av a er? : "))
b = int(input("Verdien av b er? : "))
omkrets_sirkel = 2*np.pi*a
hypotenus = np.sqrt(a**2 + b**2)
omkrets_trekant = a+b+hypotenus
omkrets_figur = omkrets_sirkel/2 + omkrets_trekant-a
print(omkrets_figur)
