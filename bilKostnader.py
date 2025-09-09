# Arbeidskrav 1 til Py1010 høst 2025

kmPerAr = 10000                     # km/år
traffikavgift = 8.38 * 365          # 8.38 per dag i 1 år
eForsikring = 5000                  # kr/år
bForsikring = 7500                  # kr/år
stromPris = 2.00                    # kr/kWh
stromPrisPerKm = stromPris * 0.2    # kWh/km
eDrivstoff = stromPrisPerKm * kmPerAr      
bDrivstoff = 1 * kmPerAr            # 1kr per km
eBom = 0.1 * kmPerAr        
bBom = 0.3 * kmPerAr

eKostnad = traffikavgift + eForsikring + eDrivstoff + eBom
bKostnad = traffikavgift + bForsikring + bDrivstoff + bBom

print("I løpet av ett år vil en elbil koste",eKostnad)
print("Sammenlignet vil en bensinbil koste",bKostnad)
print("Differansen er",round(max(bKostnad,eKostnad)-min(bKostnad,eKostnad)))
