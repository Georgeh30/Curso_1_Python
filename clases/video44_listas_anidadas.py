# LISTAS ANIDADAS O LISTAS DE 2 DIMENSIONES
# PUEDEN SER CONBINADAS, ENTRE, NUMEROS, LETRAS, SIGNOS, ETC...
# PUEDEN SER DE DISTINTOS TAMAÑOS

lista_dimensional = [

    [1, 2, 3, 4],
    [5, 6, 7],
    [8, 9, 10, 11],
    [12],
    [13, 14, 15, 16, 17, 18],
    ["H", "O", "L", "A"]

]

# INTERACION PARA  MOSTRAR CADA UNO DE LOS DATOS
for fila in lista_dimensional:
    for columna in fila:
        print(columna)

print("\n")

x = 0
y = 0

# Una forma burda de obtener la coordenadas
for fila in lista_dimensional:
    for columna in fila:
        print(x, y)
        y += 1
    x += 1

print("\n")

coordenada = ""

# Obtenemos las coordenadas y el valor de la posicion de una lista bidimensional o anidada
for n_fila in range(len(lista_dimensional)):
    for n_columna in range(len(lista_dimensional[n_fila])):
        coordenada += "[{0}, {1}] = {2} ".format(str(n_fila), str(n_columna), str(lista_dimensional[n_fila][n_columna]))
    print(coordenada)
    coordenada = ""