"""
Arbeidskrav 2 - Oppgave 2

Cathrine L. Fjeldstad (hei@calif.no)
Oppdatert: Tue Oct  7 17:41:06 2025
"""
import math

antall_elever = int(input("Hvor mange elever skal ha pizza? "))
antall_pizza = math.ceil(antall_elever/4)  #ceil-funksjonen runder opp til nærmeste heltall
print("Det må kjøpes inn", antall_pizza, "pizzaer.")