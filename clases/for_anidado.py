# EJERCICIO DE CREAR UN CUADRO CON EL NUMERO DE LADOS DADO POR EL USUARIO
try:
    n = int(input("\nIngrese el numero de lados: "))
except ValueError as e:
    print("Error!!, Valor invalido para asignar el numero de lados/", e)
cuadro = ""

try:
    for f in range(n):
        for c in range(n):
            cuadro += "*  "
        print(cuadro)
        cuadro = ""
except NameError as e:
    print("Valor no valido para asignar el rango/", e)
