"""
Prosjektoppgaven - Support Dashboard

Her utføres diverse analyser av data som er loggført 
for supportavdelingen ved telefonselskapet MORSE.

Oppdatert: Sat Mar  7 11:38:21 2026
"""
print("\nVelkommen til M O R S E support dashboard. Ha en fin dag!\n")

# ------------------- Oppgave A start -------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = "support_uke_24.xlsx"  # Navn på fila
data = pd.read_excel(file)  # Leser excel fila til en dataframe

# Lager array-er av verdiene i de ulike kolonnene i tabellen
u_dag = data["Ukedag"].to_numpy()
kl_slett = data["Klokkeslett"].to_numpy()
varighet = data["Varighet"].to_numpy()
score = data["Tilfredshet"].to_numpy()

# ------------------- Oppgave A slutt -------------------


# ------------------- Oppgave B start -------------------

# Definerer rekkefølgen på ukedagene
ukedag_orden = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]

# Lager to tomme array for ukedager og antall henvendelser
ukedager = []
antall_henvendelser_dag = []

# Går gjennom "u_dag" og teller hver forekomst av hver ukedag
for dag in ukedag_orden:
    antall = np.sum(u_dag == dag)  # Teller hvor mange ganger "dag" finnes i "u_dag".
    
    if antall > 0:  # Legger bare til dager som faktisk finnes i "u_dag"
        ukedager.append(dag)
        antall_henvendelser_dag.append(antall)  
        

# Lager en figur, et stolpediagram
plt.figure(1, figsize=(5,5))
stolper = plt.bar(ukedager, antall_henvendelser_dag, width=0.6, color="purple")
plt.yticks([])  # Fjerner tallene på y-aksen
plt.bar_label(stolper)  # viser verdiene på stolpene

plt.title("Antall henvendelser per ukedag")  # Legger tittel på diagrammet

# ------------------- Oppgave B slutt -------------------


# ------------------- Oppgave C start -------------------

# Finner min og maks
min_varighet = min(varighet)
maks_varighet = max(varighet)

# En liten funksjon som tygger tekst for å printe penere
def hent_tid(tids_str):
    h, m, s = map(int, tids_str.split(":"))
    deler = []
    
    if h > 0:
        tekst = "time" if h == 1 else "timer"
        deler.append(f"{h} {tekst}")
    
    if m > 0:
        tekst = "minutt" if m == 1 else "minutter"
        deler.append(f"{m} {tekst}")
        
    if s > 0 or not deler:
        tekst = "sekund" if s == 1 else "sekunder"
        deler.append(f"{s} {tekst}")
        
    # Limer sammen med "og" mellom alle ledd
    return " og ".join(deler)

print("--- Ukens korte og lange supportsamtale ---")

print(f"Korteste: {hent_tid(min_varighet)}")
print(f"Lengste: {hent_tid(maks_varighet)}")
print("")

# ------------------- Oppgave C slutt -------------------


# ------------------- Oppgave D start -------------------

# Gjennomsnittlig samtaletid basert på alle henvendelser i uke 24

# Finner antall henvendelser ved å sjekke lengde på variabelen
antall_henvendelser = len(data)
supporttid = pd.to_timedelta(varighet).sum()  # Gjør om til timedelta og summerer
varighet_gjennomsnitt = (supporttid/antall_henvendelser).seconds  # Regner gjennomsnitt og gjør om til sekunder
time = varighet_gjennomsnitt // 3600  # Finner antall timer fra sekunder
minutt = (varighet_gjennomsnitt % 3600) // 60  # Finner minutter fra sekunder (modulo)
sekund = varighet_gjennomsnitt % 60  # Finner resterende sekunder vha modulo

print(f"Gjennomsnittslig supporttid er: {time:02}:{minutt:02}:{sekund:02}")

# ------------------- Oppgave D slutt -------------------

# ------------------- Oppgave E start -------------------

# Gjør om klokkeslettene til pandas datetime-format
tidspunkt = pd.to_datetime(kl_slett, format="%H:%M:%S")
timer = tidspunkt.hour  # Henter ut kun time-tallet fra klokkeslettene

# Definerer gruppene klokkeslettene skal sorteres i
kl_bins = [8, 10, 12, 14, 16]  # Setter grensene for bolkene
kl_labels = ["kl 08-10", "kl 10-12", "kl 12-14", "kl 14-16"]  # Setter navn på bolkene

# Sorterer klokkeslettene i grupper (bins)
tidsblokker = pd.cut(timer, bins=kl_bins, right=False, labels=kl_labels)
# Teller frekvensen på hver gruppe
antall_henvendelser_bolk = tidsblokker.value_counts().sort_index()

# Lager en ny figur, et kakediagram
plt.figure(2, figsize=(5,5))
# antall_henvendelser_bolk.plot.pie(autopct="%.1f%%", startangle=90)
antall_henvendelser_bolk.plot.pie(
    # en liten funksjon som viser både faktisk verdi og prosent i kakediagrammet
    autopct=lambda pct: f"{int(round(pct*antall_henvendelser_bolk.sum()/100))}\n({pct:.1f}%)",
    startangle=90
)
plt.ylabel("")  # Tømmer label på y-aksen
plt.title("Antall henvendelser per supportvakt")
plt.show()
 
# ------------------- Oppgave E slutt -------------------

# ------------------- Oppgave F start -------------------

# Tilfredshetskalaen går fra 1 Svært misfornøyd til 10 Svært fornøyd
# NPS score
NPS_scores = score[~np.isnan(score)]  # Fjerner alle uten verdi (nan)
antall_feedback = len(NPS_scores)  # Hernter antall tilbakemeldinger

NPS_bins = [1, 7, 9, 11]  # Setter grenseverdier
NPS_labels = ["detractors", "passives", "promoters"]  # Gir grensene navn

# Sorterer tilbakemeldingene i grupper (bins)
feedback = pd.cut(NPS_scores, bins=NPS_bins, right= False, labels=NPS_labels)
# Teller frekvensen på hver gruppe
feedback_frekvens = feedback.value_counts().sort_index()

# Mellomlagrer verdiene for detractors og promoters i prosent
detractors = (feedback_frekvens["detractors"]/antall_feedback)*100
promoters = (feedback_frekvens["promoters"]/antall_feedback)*100
# Regner ut NPS score, %promoters - %detractors, og runder av
NPS_score = round(promoters-detractors)

print(f"NPS-score er: {NPS_score}")

# ------------------- Oppgave F slutt -------------------






