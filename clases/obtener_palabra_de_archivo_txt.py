# Archivos de texto

archivo = open("ejemplo.txt", "r")  # r --> abrir, r+ --> abrir y leer, w --> crear nuevo archivo

lista_anidada = []  # Inicializo List sin datos

# Interando por linea de texto
for linea in archivo.readlines():  # Convertimos el texto del archivo (archivo.readlines()) en una list guardandolo en la variable (linea)
    lista = []  # Inicializo List sin datos
    for palabra in linea.split(" "):  # Separamos el primer dato por palabras (linea.split(" ")) y lo guardamos en la variable (palabra)
        lista.append(palabra)  # Guardamos la palabra en la list creada antiormente (lista.append(palabra))
    lista_anidada.append(lista)  # Al salir del ciclo for guardamos la lista anterior dentro de una lista nueva lista_anidada.append(lista)

print(lista_anidada)  # Imprime la lista anidada completa
print(lista_anidada[0][3])  # Imprime solo una palabra dandole las coordenadas dentro de la lista anidada

archivo.close()  # Debemos Cerrar el archivo al finalizar el proceso