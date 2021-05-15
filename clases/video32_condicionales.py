def edad(m=0):
    if m == 18:
        c = "Tiene 18 años"

    elif m > 18:
        c = "Es mayor de Edad"

    elif 1 <= m < 18:
        c = "Es menor de Edad"

    else:
        c = "Dato No ingresado"

    return c


dato = edad(100)
print(dato)


def comparacion(valor=0):
    if valor > 0:
        print(valor)
        return True
    else:
        print(valor)
        return False


#Ejemplo de otra forma de llamar una funcion, en este caso dentro de una condicion if
if comparacion(0):
    print("La funcion es igual a True")
else:
    print("La funcion es igual a False")

