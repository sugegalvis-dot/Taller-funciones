"""
Ejercicio 1
Crea una funcion para área de un triangulo por base y altura
"""
areas = 0
def area (base, altura):
    if base <= 0 or altura  <= 0:
        return None
    area = (base * altura) / 2
    return area



while True:
    for i in range (2):
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))

        if i == 0:
            area1 = area (base, altura)
        else: 
            area2 = area (base, altura)
    break

print("Áreas: ", area1, area2)
print("Suma: ", area1 + area2)

