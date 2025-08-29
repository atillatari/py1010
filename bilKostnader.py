kmPerAr = 10000
traffikavgift = 8.38 * 365  # 8.38 per dag i 1 år
eForsikring = 5000
bForsikring = 7500
eDrivstoff = 0.2 * kmPerAr  # kWh/km
bDrivstoff = 1 * kmPerAr    # 1kr per km
eBom = 0.1 * kmPerAr        
bBom = 0.3 * kmPerAr

eKostnad = traffikavgift + eForsikring + eDrivstoff + eBom
bKostnad = traffikavgift + bForsikring + bDrivstoff + bBom

print("I løpet av ett år vil en elbil koste " + str(eKostnad) + ",-")
print("sammenlignet vil en bensinbil koste  " + str(bKostnad) + ",-")
print("Differansen er " + str(round(max(bKostnad,eKostnad)-min(bKostnad,eKostnad))) + ".")
