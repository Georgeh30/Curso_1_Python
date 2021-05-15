# Archivos de texto

archivo = open("ejemplo.txt", "r")  # r --> abrir, r+ --> abrir y leer, w --> crear nuevo archivo, w+ --> escribir y leer

#  print(archivo.readable())  # Para confimar que no este dañado
#  print(archivo.read())  # Para mostrar en consola el contenido del texto
#  print(archivo.readline())  # Para mostar solamente la primera linea del texto

#  print(archivo.readlines())  # Devuelve una lista (arreglo) con todos los datos del texto y podemos pedir solo un dato
#  print(archivo.readlines()[5])  # Devuele solo la posicion 5 dentro de la lista

'''lista_anidada = []
# Interando por linea de texto
for linea in archivo.readlines():
    lista = []
    for palabra in linea.split(" "):
        lista.append(palabra)
    lista_anidada.append(lista)

print(lista_anidada)
print(lista_anidada[0][3])'''

archivo.close()