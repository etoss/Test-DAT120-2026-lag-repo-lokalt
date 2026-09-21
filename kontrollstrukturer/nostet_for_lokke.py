for time in range(1, 24):
    print(time)
    for minutt in range(1, 60):
        print(f"{time}:{minutt}")
        for sekund in range(1, 60):
            print(f"{time}:{minutt}:{sekund}")

# Antall ganger linje 4 kjører er 6*3 = 18