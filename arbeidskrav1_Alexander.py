# Arbeidskrav 1 
# Beregning av de årlige kostnadene for elbil og bensinbil
# Oppgaven går ut på finne den årlig kostnadssdifferanse
# Elbil VS Bensinbil



# Faste parametere
antall_km = 10000  # Forutsetter at antall km er 10000 for el og bensin bilen
forsikring_el = 5000 
forsikring_bil = 7500


# kostnader basert pÃ¥ antall km
trafikkforsikringsavgift = 8.38 * 365  # Ganger satsen med antall dager i et år
drivstoffbruk_elbil = 0.2 * 2 
drivstoffbruk_bensinbil = 1 
bomavgift_elbil = 0.1
bomavgift_bensinbil = 0.3

# Kalkulasjon av kostnadene
EL_drivstoff = antall_km * drivstoffbruk_elbil
Bensinbil_drivstoff = antall_km * drivstoffbruk_bensinbil
El_bomavgift = antall_km * bomavgift_elbil
bensin_bomavgift = antall_km * bomavgift_bensinbil  



# Utregning
elbil = forsikring_el + trafikkforsikringsavgift + EL_drivstoff + El_bomavgift
bensinbil = forsikring_bil + trafikkforsikringsavgift + Bensinbil_drivstoff + bensin_bomavgift



print(f"Den årlige kostnaden for en elbil er kr {elbil}"
      f" sammenlignet med kr {bensinbil} for bensinbil."
      f" Den årlige Kostnadsdifferansen mellom en elbil og bensin bil er {bensinbil - elbil} kr"
      f" rimligere for enn elbil enn en bensinbil")