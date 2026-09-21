# Script for å regne ut volum av et rom

def skriv_inn_positivt_tall(beskjed):
    mangler_verdi = True
    while mangler_verdi:
        try:
            positivt_tall = float(input(beskjed))
        except ValueError:
            print("Du må skrive inn et tall")
            continue
        if positivt_tall < 0.0:
            print("Tallet må være positivt")
        else:
            mangler_verdi = False
    return positivt_tall


# Hviv dette er scriptet som kjøres, utfør denne blokken.
# Hvis dette scriptet blir importert fra et annet script, ikke utfør denne blokken.
if __name__ == "__main__":
    lengde = skriv_inn_positivt_tall("Skriv inn lengde: ")
    bredde = skriv_inn_positivt_tall("Skriv inn bredde: ")
    hoyde = skriv_inn_positivt_tall("Skriv inn høyde: ")
    volum = lengde*bredde*hoyde
    print(f"Volumet på rommet er: {volum}")
