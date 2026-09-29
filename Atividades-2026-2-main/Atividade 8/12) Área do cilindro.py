pi = 3.14

r = float(input("Raio: "))
h = float(input("Altura: "))

area_base = pi * r**2
area_lateral = 2 * pi * r * h

area_total = 2 * area_base + area_lateral
print("Área:", area_total)