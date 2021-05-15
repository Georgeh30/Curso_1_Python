# ESTE PROGRAMA GUARDA OBJETOS TIPO ESTUDIANTE DENTRO DE UNA CLASE TIPO LISTA ESTUDIANTE
# DENTRO DE UN ARCHIVO TIPO BINARIO CREADO SI ES QUE NO EXITE Y AGREGANDO CADA QUE SE EJECUTA MAS
# DATOS EN EL Y MOSTRANDOLOS EN CONSOLA

from video66_proyecto.estudiante import Estudiante
import pickle

estudiante1 = Estudiante("Jorge", 28, "Python")
estudiante2 = Estudiante("Josue", 21, "Java")


class ListaEstudiantes:
    estudiantes = []

    def __init__(self):
        archivoEstudiantes = open("Lista_estudiantes", "ab+")  # a de abrir, b de tipo binario y + de lectura
        archivoEstudiantes.seek(0)  # Paea poner el apuntador o cursor que seleccione la primeora posicion 0 del archiv

        try:
            self.estudiantes = pickle.load(archivoEstudiantes)  # Cargamos los datos en la variable de tipo lista
            print(f"{len(self.estudiantes)} estudiantes cargados correctamente")
        except EOFError as e:
            print(e)
            print("No se han cargado estudiantes previos")
        finally:
            archivoEstudiantes.close()
            del archivoEstudiantes  # Para elimiar el espacio guardado dentro de esta variable

    def agregarEstudiante(self, e):
        self.estudiantes.append(e)
        self.guardarEstudiantes()  # Mandamos a llamar el metodo de abajo

    def guardarEstudiantes(self):
        archivo = open("Lista_estudiantes", "wb")  # w de escribir y b de forma binaria
        pickle.dump(self.estudiantes, archivo)  # Para guardar datos de tipo objeto, almacenando la lista en el archivo
        archivo.close()
        del archivo

    def __str__(self):
        valor = ""
        for e in self.estudiantes:
            valor += str(e) + "\n"
        return valor


#CREAMOS UN OBJETO DE LA CLASE LISTAESTUDIANTES
lista_estudiante = ListaEstudiantes()

# AGREGANDO NUEVOS ESTUDIANTES DE LA CLASE ESTUDIANTE
lista_estudiante.agregarEstudiante(estudiante1)
lista_estudiante.agregarEstudiante(estudiante2)

# IMPRIMIMOS LOS DATOS OBTENIDOS DE LOS OBJETOS AGREGADOS
print(lista_estudiante)
