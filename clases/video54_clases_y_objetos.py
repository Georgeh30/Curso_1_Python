
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


estudiante1 = Estudiante("Jorge", 28, "Python")  # Objeto de tipo Estudiante

estudiante1.edad = 29  # Podemos ir cambiando el valor de algun atributo
estudiante1.cursos.append("Java")  # Para ir agregando varios datos al atributo tipo list
estudiante1.cursos.append(["Java Script", "C++"])  # Agrega una sublista
estudiante1.cursos.extend(["C#", "Go"])  # Para agregar varios datos a la misma list

print(estudiante1.edad)  # Podemos imprimir en consola un dato de esta forma

# Podemos imprimir toda la informacion de los atributos de...
# este objeto pero solo si se agrego el metodo especial __str__, el cual es el toString
print(estudiante1)

# Mandamos a llamar el metod creado por nosotros para eliminar un curso en especifico
print(estudiante1.eliminar_curso("C#"))
print(estudiante1)  # Volvemos a imprimir los datos para verificar que ha sido eliminado
