# Lag et script som leser inn en prosentscore og skriver ut hvilken bokstavkarakter
# det tilsvarer.

fortsetter = True
while fortsetter:
    prosentscore = float(input("Skriv inn en prosentscore: "))

    if prosentscore < 0 or prosentscore > 100:
        break       # Avslutter while-løkka

    if prosentscore >= 90:
        print("A")
    elif prosentscore >= 80:
        print("B")
    elif prosentscore >= 60:
        print("C")
    elif prosentscore >= 50:
        print("D")
    elif prosentscore >= 40:
        print("E")
    else:
        print("F")
