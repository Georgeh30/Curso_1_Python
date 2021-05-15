import pickle

# 1. SERIALIZAR COLECCIONES
estudiantes = [
    "Marcos",
    "Karla",
    "Alfonso",
    "Pedro",
    "Maria"
]

# CREACION DE ARCHIVO Y GUARDADO DE LA SERIALIZACION DE LA LISTA DE ARRIBA
archivo_serializado = open("estudiantes", "wb")  # Creamos y Abrimos el archivo dandole permiso de escritura (w) y de binatio (b)

pickle.dump(estudiantes, archivo_serializado)

archivo_serializado.close()
del archivo_serializado  # Sirve para eliminar el archivo de la memoria de python porque ya no la vamos a usar dentro de python
# FIN DE CREAR ARCHIVO SERIALIZADO




# ABRIENDO, LEYENDO Y RECONSTRUYENDO EL ARCHIVO SERIALIZADO A NUEVAMENTE UNA LIST
archivo = open("estudiantes", "rb")  # Indicamos que queremos solo leer (r) el archivo del tipo binario (b)

lista_estudiantes = pickle.load(archivo)

print(lista_estudiantes)
# FIN DE LEER ARCHIVO SERIALIZADO
