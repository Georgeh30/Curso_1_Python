#EN LAS LIST SE PUEDE MEZCLAR DISTINTOS TIPOS DE ATRIBUTOS O VARIABLES, YA SEAN INT, STRING, BOOLEAN, ETC...
#EN LAS LIST SE PUEDE IR MODIFICANDO LOS DATOS Y EN LAS TUPLAS SON ESTATICAS

#Forma como crear la list
frutas = ["manzana","sandia","melon","uva","pera","durazno","guayaba","papaya","piña","limon"]

print("Estos son los datos guardados en a lista: ", frutas) #imprimimos la lista completa
print(frutas[5]) #mostramos solo la posicion indicada
print(frutas[-1]) #mostramos el dato de la ultima posicion
print(frutas[2:7]) #mostramos los datos desde la posicion 2 hasta antes de la posicion 7
print(frutas[6:]) #mostramos los datos desde la posicion 6 hasta la final
print(frutas[:3]) #mostramos los datos desde la incial hasta una antrs de la 3

#ALGUNAS FUNCIONES DE LA LIST
#list, len, append, extend, insert, remove, clear, pop, index, count, sort, reverse, copy

#Otra opcion para crear una lista es guardandola dentro de un string
lista = list(("hola","mundo","soy","jorge", 2, 2.3, 10+0j, bool, True, int, str, -0.3, [5, "hola"])) #lista conbinada
print(lista)

lista[3] = "Jorge" #Modifica el dato de la posicion indicada

listamezclada = lista + frutas #Mezcla dos o mas listas en una sola
print(listamezclada)

lista.append("kk") #Para agregar un nuevo dato a la lista pero si son mas de uno se agrega como una lista dentro de esta otra lista
lista.extend([1, 3]) #Hace lo mismo que append pero agrega mas de un dato sin crear una sulista
tamano = len(lista) #Para obtener el tamaño de la lista
print(lista)
print(tamano)

listainsert = ["Uno", "Dos", "Tres", 4, 4.5, 5]
listainsert.insert(0, "Cero")
print(listainsert)

lista.remove('mundo') #Eliminamos el dato indicado

lista.pop(0) #Eliminamos el dato del indice indicado

lista.pop() #Eliminamos el ultimo dato de la lista

print("Lista con dato eliminado:", lista)
print("Asi podemos retornar el elemento eliminado:", lista.pop(3)) #Eliminamos por posicion y mostramos el elemento eliminado

lista.reverse() #Invierte el orde de la lista
print("Invierte el orden de la lista:", lista)

listanueva = ["Ana", "Jorge", "Linette", "Josue", "Juan", "Maria", "Jorge"]
listanueva.sort() #Ordena por letra o numero de forma ascendente
print(listanueva)

listanueva.sort(reverse=True) #Ordena por letra o numero de forma descendente
print(listanueva)

repetidos = listanueva.count("Jorge") #Cuenta cuantas veces aparece el mismo dato dentro del list
print(repetidos)


lista123 = ["Kart", "Lol", "Mam", "Cool", "Lol"]
print(lista123)

posicion = lista123.index("Lol") #Obtiene la posicion del primer valor que coicida con el solicitado
print(posicion)

posicion_inicio_final = lista123.index("Lol", 4, 5) #Obtiene la posicion del valor buscado entre la coma numero 4 y el corchete final
print(posicion_inicio_final)

copia = lista123.copy() #Copia los datos a otra variable
print(copia)

lista123.clear() #Elimina todos los datos dentro de la list
print(lista123)