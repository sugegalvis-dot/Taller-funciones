"""
Ejercicio 4
Cree una función para pago semanal con horas extra.
"""

def pago_Sem (horas, tarifa):
    if horas <=40:
        pago = horas * tarifa
        
    elif horas > 40:
        pago = 40 * tarifa + (horas - 40)* tarifa * 1.5
    return pago

for i in range (2):
    horas = float(input("Horas "+str(i+1)+":"))
    tarifa = float(input("Tarifa "+str(i+1)+":")) 

    if i == 0:
        hora1 = horas
        tarifa1 = tarifa
    else: 
        hora2 = horas
        tarifa2 = tarifa

p1 = pago_Sem (hora1, tarifa1)
p2 = pago_Sem (hora2, tarifa2)

print ("pagos: ", p1, p2, "Total: ", p1 + p2)
