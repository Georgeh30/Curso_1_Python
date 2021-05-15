import pickle


class Estudiante:

    # Este metodo es el Constructor y tiene doble __ al principio y al final que indica que es un metodo especial
    def __init__(self, nombre, edad, curso_inicial):
        # Inicializamos las variables o atributos, aunque hay atributos que puede ya tener definido un dato por default
        self.nombre = nombre
        self.edad = edad
        self.curso_inicial = curso_inicial
        self.esta_activo = True
        self.cursos = [curso_inicial]

    def eliminar_curso(self, curso):
        self.cursos.remove(curso)
        return "Dato eliminado"

    def __str__(self):
        return "Nombre: " + self.nombre + ", Edad: " + str(self.edad) + ", Curso Actual: " + self.curso_inicial \
               + ", Estatus: " + str(self.esta_activo) + ", Cursos: " + str(self.cursos)


estudiante1 = Estudiante("Jorge", 28, "Python")
estudiante2 = Estudiante("Eduardo", 22, "Java")
estudiante3 = Estudiante("Mario", 29, "C++")

lista_objetos_estudiante = [
    estudiante1,
    estudiante2,
    estudiante3
]

archivo_serializado_objeto_estudiante = open("estudiantes_obj", "wb")

pickle.dump(lista_objetos_estudiante, archivo_serializado_objeto_estudiante)

archivo_serializado_objeto_estudiante.close()
del archivo_serializado_objeto_estudiante




# ABRIENDO, LEYENDO Y RECONSTRUYENDO EL ARCHIVO SERIALIZADO A NUEVAMENTE UNA LIST
archivo = open("estudiantes_obj", "rb")  # Indicamos que queremos solo leer (r) el archivo del tipo binario (b)

lista_estudiantes = pickle.load(archivo)

print(lista_estudiantes)

for estudiante in lista_estudiantes:
    print(estudiante)

# FIN DE LEER ARCHIVO SERIALIZADO
