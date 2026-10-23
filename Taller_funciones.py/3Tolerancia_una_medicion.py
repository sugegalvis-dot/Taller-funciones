"""
Ejercicio 3
Cree las funciones necesarias para la tolerancia de una medicion

-funcion de valor absoluto que -> Recibe un real y devuelve su distancia al cero
-Los extremos de tolerancia se aceptan.
-La funcion de aceptacion utiliza el retorno de valor absoluto
-Consulta dos mediciones por separado
-
Contratos en orden de parametros: 
Valor absoluto: -> Recibe real finito y devuelve real NoNegativo

Aceptación: -> Recibe medición y objetivos reales,
tolerancia real no negativa y devuelve lógico.

"""

def Valorabs (x):
    if x < 0:
        return -x
    return x


def verif (medicion, objetivo, tolerancia):
    error = Valorabs (medicion - objetivo)
    return error <= tolerancia

objetivo = float(input("Objetivo: "))
tolerancia = float(input("Tolerancia: "))

for m in range (2):
    medicion = float(input("medicio: "))
    if m ==0:
        m1 = medicion
    else: 
        m2= medicion

r1 = verif (m1, objetivo, tolerancia)
r2 = verif (m2, objetivo, tolerancia)

print ("Aceptables:", r1, ",", r2)
