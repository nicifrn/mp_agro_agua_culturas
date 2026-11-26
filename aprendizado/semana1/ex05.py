import math

graus = float(input("Graus: "))
minutos = float(input("Minutos: "))
hemisferio = input("Hemisfério (norte/sul): ").strip().lower()

graus_decimais = graus + minutos / 60
radianos = graus_decimais * math.pi / 180

if hemisferio == "sul":
    radianos = -abs(radianos)

print(round(radianos, 2))