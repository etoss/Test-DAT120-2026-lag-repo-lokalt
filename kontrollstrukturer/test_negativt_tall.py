tall_str = input("Skriv inn et tall: ")
tall_float = float(tall_str)

if tall_float < 0.0:        # Hvis tall_float er mindre enn 0,0
    print("Tallet er negativt")
    print("En print-setning til")
elif tall_float == 0:       # Ellers, hvis tall_float er lik 0
    print("Tallet et 0")
else:                       # Ellers
    print("Tallet er positivt")
print("Skrives ut uansett")
