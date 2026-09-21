# Lag et script som leser inn en prosentscore og skriver ut hvilken bokstavkarakter
# det tilsvarer.

def finn_bokstavkarakter(prosentscore):
    if prosentscore >= 90:
        return("A")
    elif prosentscore >= 80:
        return("B")
    elif prosentscore >= 60:
        return("C")
    elif prosentscore >= 50:
        return("D")
    elif prosentscore >= 40:
        return("E")
    else:
        return("F")


def test_finn_bokstavkarakter():
    # Test alle veier gjennom funksjonen
    karakter = finn_bokstavkarakter(90)
    if karakter != "A":
        print(f"Test feiler: 90 poeng gav ikke A, men {karakter}")
    karakter = finn_bokstavkarakter(80)
    if karakter != "B":
        print("Test feiler")
    karakter = finn_bokstavkarakter(60)
    if karakter != "C":
        print("Test feiler")
    karakter = finn_bokstavkarakter(50)
    if karakter != "D":
        print("Test feiler")
    karakter = finn_bokstavkarakter(40)
    if karakter != "E":
        print("Test feiler")
    karakter = finn_bokstavkarakter(20)
    if karakter != "F":
        print("Test feiler")
    # Test grenseverdier
    karakter = finn_bokstavkarakter(89)
    if karakter != "B":
        print("Test feiler")
    karakter = finn_bokstavkarakter(79)
    if karakter != "C":
        print("Test feiler")
    karakter = finn_bokstavkarakter(59)
    if karakter != "D":
        print("Test feiler")
    karakter = finn_bokstavkarakter(49)
    if karakter != "E":
        print("Test feiler")
    karakter = finn_bokstavkarakter(39)
    if karakter != "F":
        print("Test feiler")


test_finn_bokstavkarakter()
