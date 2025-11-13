"""
Arbeidskrav 2 - Oppgave 4
Oppdatert: Tue Oct  7 17:57:58 2025
"""
data = {
        "Norge": ["Oslo", 0.634],
        "England": ["London", 8.982],
        "Frankrike": ["Paris", 2.161],
        "Italia": ["Roma", 2.873]
        }

land = input("Skriv inn navnet på et land: ")

if land in data:
    print(f"{data[land][0]} er hovedstaden i {land} og det er",
          f"{data[land][1]} mill. innbyggere i {data[land][0]}.")
    
else:
    svar = input("Dette landet finnes ikke i databasen. Vil du legge det til? ")
    if svar in ("ja", "j", "J", "JA", "Ja", "Ok", "OK"):
        hovedstad = input(f"Hovedstaden i {land} er? ")
        antall_inbyggere = input(f"Antall millioner innbyggere i {hovedstad} er? ")
        data[land] = [hovedstad, antall_inbyggere]
        print(data)
    else:

        print("Ok, takk for nå!")
        
