# Archivo de texto

# Crear, Escribir y Modificar

#Crear
archivo_nuevo = open("nuevo.txt", "w")  # La letra w indica que vamos a crear un archivo nuevo con el nombre nuevo.txt

print(archivo_nuevo.writable())  # Sirve para confirmar si tenemos permisos de escritura
print(archivo_nuevo.write("Al crear el archivo de texto\n"
                          "le vamos a agregar este texto con el metodo (write),\n"
                          "el cual nos devuelve el numero de espacios ocupados y\n"
                          "nos creara el archivo en la ruta general dentro del proyecto.\n"))

archivo_nuevo.close()

#Agregar contenido
archivo_nuevo = open("nuevo.txt", "a")  # La letra a indica que vamos a agregar o escribir mas texto

print(archivo_nuevo.write("Estamos agregando este text nuevo\n"
                          "al archivo ya creado anteriormente\n"))

archivo_nuevo.close()
