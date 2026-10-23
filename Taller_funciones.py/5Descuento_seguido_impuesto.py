"""
Ejercicio 5:
Cree las funciones necesarias seguido del impuesto ficticio
"""

def subtotal_descuento (base, descuento):
    if base >= 0 and 0 <= descuento <= 100:
        subtotal= base * (1- descuento/100)
        return subtotal

def total (subtotal, impuesto):
    if subtotal > 0 and impuesto > 0:
        total= subtotal *(1+impuesto/100)
        return total

    base= float(input("Base: "))
    descuento = float(input("Descuento: "))
    impuesto = float(input("Impuesto: "))

    subtotal= subtotal_descuento (base, descuento)
    total = total (subtotal, impuesto)

    if subtotal and total != None:
        print("subtotal: ", subtotal_descuento(base, descuento))
        print ("Total: ", total(subtotal, impuesto), str("en pesos"))

    else: 
        print ("subtotal: 0; Total: 0")