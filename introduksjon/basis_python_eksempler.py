# Lager variabelen "et_tall" og setter den lik 7
et_tall = 7

# Skriver ut innholdet i variabelen et_tall
print(et_tall)

# Lager variabelen "tall_to" og setter den lik 5
tall_to = 5

# Skriver ut begge tallene
print(tall_to)
print(et_tall)

# Lager variabelen tall_tre og setter den lik summen av innhldet i et_tall og tall_2
tall_tre = et_tall + tall_to
print(tall_tre)

# Lager en variabel flyttall, setter den lik 0.1, og skriver den ut
flyttall = 0.1
print(flyttall)

# Viser hvordan flyttall kan oppføre seg merkelig på grunn av binære avrundingsfeil
flyttall = flyttall + 0.1
print(flyttall)
flyttall = flyttall + 0.1
print(flyttall)

# Minus operatoren, kan fint ha negative tall
print(5-8)

# Heltallsdivisjon //, hvor mange ganger går 3 opp i 8?
print(8//3)

# Flyttallsdivisjon /
print(8/3)

# Heltallsdivisjon runder alltid ned
print(-8//3)
-3

# Modulo operatoren gir resten etter en heltallsdivisjon
print(8%3)
2

# Opphøying
print(2**3)

# float funksjonen for å konvertere til flyttall
test = float(5)
print(test)

# int funksjonen for å konvertere til et heltall. Kapper bare bort det bak komma.
test = int(6.7)
print(test)

# round funksjonen runder av flyttall
test = round(5/3) 
print(test)

# Runder av til 2 desimaler
test = round(5/3, 2)
print(test)

# Importerer math pakkel
import math

# Eksempel på bruk av funksjonen sin (sinus). Denne funksjonen tar vinkler målt i radianer
test = math.sin(2)
print(test)

# math.pi er flyttallet som er nærmest pi.
print(math.pi)
