"""
Arbeidskrav 2 - Oppgave 2
Oppdatert: Tue Oct  7 17:41:06 2025
"""
import math

antall_elever = int(input("Hvor mange elever skal ha pizza? "))
antall_pizza = math.ceil(antall_elever/4)  #ceil-funksjonen runder opp til nærmeste heltall

if antall_pizza == 1:
    print(f"Det må kjøpes inn {antall_pizza} pizza.")
else:
    print(f"Det må kjøpes inn {antall_pizza} pizzaer.")
