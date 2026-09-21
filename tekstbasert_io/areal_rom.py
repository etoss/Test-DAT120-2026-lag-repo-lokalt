# Dette er en kommentar. Tolkeren hopper over denne linja.
lengde_str = input("Skriv inn lengden til rommet: ")
bredde_str = input("Skriv inn bredden til rommet: ")
lengde_m = float(lengde_str)
bredde_m = float(bredde_str)
areal = lengde_m*bredde_m
#areal = round(areal, 2)
print(f"Arealet av et rom med lengde {lengde_m} \t og bredde {bredde_m} \n er: {areal:7.2f}")
