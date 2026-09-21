# Lag et script som lar brukeren skrive inn flere linjer tekst og hvor
# brukeren avslutter ved å skrive inn ei tom linje.

# Alltid tenk over hvordan ei løkke skal slutte!

TYNGDEAKSELLERASJON = 9.8   # Konstant, konvensjon at de er i ALL CAPS

hele_teksten = ""           # Akkumulator
antall_linjer = 0           # Teller
nv_linje = "Startverdi"     # Verdilagrer - lagrer siste verdi fra brukeren
while nv_linje != "":       # Så lenge nv_linje er ulik en tom streng, utfør blokka
    nv_linje = input("Skriv inn ei linje: ")
    hele_teksten += nv_linje + "\n"   # hele_teksten = hele_teksten + nv_linje
    antall_linjer += 1
print(f"Antall linjer: {antall_linjer}")
print(hele_teksten)
