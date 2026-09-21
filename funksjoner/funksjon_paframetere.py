import math
#import forste_eksempel

from forste_eksempel import skriv_inn_positivt_tall


def areal_sirkel(radius):
    areal = math.pi*radius*radius
    return areal


arealet = areal_sirkel(5)
print(f"Arealer er: {arealet}")
arealet = areal_sirkel(7)
print(f"Arealer er: {arealet}")

arealet = areal_sirkel(skriv_inn_positivt_tall("Radius til sirkelen: "))
print(f"Arealer er: {arealet}")
