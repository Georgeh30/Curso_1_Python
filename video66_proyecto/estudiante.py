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
