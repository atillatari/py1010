"""
Arbeidskrav 2 - Oppgave 1
Oppdatert: Tue Oct  7 17:24:34 2025
"""
from datetime import date

alder = int(input("Hvilket år er du født? "))  # Spør om fødselsår og lagrer som heltall
innevarende_aar = date.today().year  # inneværende år
alder = innevarende_aar - alder
print("Gratulerer med "+str(alder)+"-årsdagen i år!")

