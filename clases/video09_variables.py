#DECLARACION DE VARIABLES
numero = 10 #tipo int
palabra = "Jorge " #tipo string
vof = False #tipo boolean
decimal = 1.25 #float
arreglo1 = ["uno", "dos", "tres"] #tipo list o array
complejo = (11.20+0j) #tipo complex

numero1, numero2, numero3 = 5, 4, 10

print(palabra + str(numero) + " " + str(vof) + " " + str(decimal))# se mete dentro de str para concatenar los distintos tipos de variables
print(int(vof))#los boolenanos tambien se devuelven como 1 o 0

#PARA OBTENER UN BOOLEANO DE UNA VARIABLE DE CUALQUIER TIPO SI TIENE O NO DATOS
print(bool(0))#para indicar si el 0 es verdadero o falso o parseo a booleano
print(bool("hola"))
print(bool(""))

#CONCATENAR Y OTROS EJEMPLOS
print(None)
print(str(numero1) + " " + str(numero2) + " " + str(numero3))
print(arreglo1[0])
print(complejo)

#Para inidicar el tipo de variable que es cada uno
print(type(numero))
print(type(palabra))
print(type(decimal))
print(type(vof))
print(type(arreglo1))
print(type(complejo))

#EL PARSEO DE LAS VARIABLES
print(int(decimal))
print(float(numero))
print(str(numero3) + " convertido a string")

help("keywords")#para ver la lista de palabras reservadas dentro de python