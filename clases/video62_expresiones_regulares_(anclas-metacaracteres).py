from re import findall

lista = [
    "Jorge - Python",
    "Mario - Java",
    "Flor - PHP",
    "Mario - C++",
    "Daniela - Python",
    "Carlos - C++",
    "C++ - Mario",
    "Java -  Daniela",
    "Carlos - Java",
    "Mario - Python, Java, Etc... - Luis",
    "Mario Luis",
    "Qué Pasa - Nada!",
    "Que Pasa - Nada!"
]


for linea in lista:
    if findall("^Mario", linea):  # Muestra las lineas donde empiece con (Mario) al poner ^ al princio de la frase
        print("Frase encontrada al principio", linea)

for linea in lista:
    if findall("Mario$", linea):  # Muestra las lineas donde termine con (Mario) al poner $ al final de la frase
        print("Frase encontrada al final", linea)

for linea in lista:
    if findall("^Mario Luis$", linea):  # Muestra solo si es exactamente desde principio a fin la cadena que buscamos
        print("Frase Exactamente como se pide:", linea)

for linea in lista:
    if findall("Qu[ée] Pasa - Nada!", linea):  # Muestra la cadena que buscamos con las dos formas que pede aparecer con acento en la (e) o sin acento en la (e)
        print(linea)
