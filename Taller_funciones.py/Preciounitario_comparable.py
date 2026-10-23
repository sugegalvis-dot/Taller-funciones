"""
Ejercicio 2
Cree una funcion para precio unitario comparable.
-Recibe precio real no negativo -> en pesos
-Cantidad positiva en gramos 
-Devuelve peso real de un gramo en pesos
"""
def precio_unit (precio_total, cantidad_gramos):
    if precio_total < 0 or cantidad_gramos < 0:
        return None
    precio_unit = precio_total / cantidad_gramos
    return precio_unit

def comparable (precio1, precio2):
    if precio1>precio2:
        return "Paquete 2"
    elif precio1 < precio2:
        return "paquete 1"
    else:
        "No hay diferencia de paquetes"

while True:
    for i in range (2):
        Precio_total = int(input("Ingrese precio total en pesos: "))
        Cantidad_gramos = int(input("Ingrese los gramos: "))
        
        if i ==0:
            Precio1 = precio_unit (Precio_total, Cantidad_gramos)
        else:
            Precio2 = precio_unit (Precio_total, Cantidad_gramos)
    break

print ("Precios por gramo: ", Precio1, ",", Precio2, "Pesos")
print ("Precio comparable: ", comparable (Precio1, Precio2))


    
