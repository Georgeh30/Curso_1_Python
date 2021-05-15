#Nos permite mapear (crear una base de datos ordenada gráficamente) valores mediante pares “clave – valor”.
#EJEMPLO: De esta forma podremos guardar “Valores” (Juan, 55, Masculino, Si, No, 4, $16000)
# en “Claves” (Nombre, Edad, Genero, Hijos, Casado, Cuantos Hijos, Ingresos) de una manera mas ordenada y accesible.

diccionario = {
  "Alemania": "Berlín",
  "Francia": "Paris",
  "Reino Unido": "Londres",
  "Mexico": "Estado de Mexico"}

print(diccionario["Alemania"]) #Muestra el dato guardado con la llave o clave llamada Alemania

#Opcion para Agregar o Modificar un Valor mediante la Clave
diccionario["Mexico"] = "Cd de Mexico" #Sirve para Modificar el valor de la Clave o Llave y para agregar otra pareja de dato
diccionario["Brasil"] = "Rio de Janeiro" #En este caso estamos agregando un dato nuevo
print(diccionario)

#Opcion para Modificar una Clave y Puede tambien eliminar un par de valores en especifico
diccionario["Holanda"] = diccionario.pop("Alemania") #Modificamos la Clave Alemania a Holanda sin cambiar el valor
print(diccionario)

indice = diccionario.keys() #Muestra Todas las Claves de cada pareja de datos
print(indice)

valor = diccionario.values() #Solo obtiene Todos los valores de cada Clave del diccionario
print(valor)

#FOR QUE RECORRE (INTERAR) E IMPRIME CADA VALOR DEL DICCIONARIO
for dato in diccionario:
  print(dato, ":", diccionario[dato])

dic = dict(nombre='nestor', apellido='Plasencia', edad=22) #Convierte estos datos si son factibles a diccionario
print(dic, type(dic))

dic2 = dict(zip('abcd',[1, 2, 3, 4])) #Solo se deben de ingresar dos parametros con la misma cantidad de caracteres y los convierte a diccionario
print(dic2)

dic3 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
items = dic3.items() #Convierte el diccionario a tupla
print(items)

dic4 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic4.clear() #Elimina todos los datos del diccionario
print(dic4)

dic5 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic6 = dic5.copy() #Realiza una copia del diccionario
print("dic6:", dic6, type(dic6))

########################
cadena = dic6 #Este No hace una copy solo cambi de nombre el directorio original
print("cadena:", cadena, type(cadena))

#Cuando solo modificamos el nombre del diccionario
cadena["d"] = 7 #Al Modificar el nuevo nombre
print("Nueva Cadena", cadena, "Anterior diccionario: ", dic6) #Nos mostrara en el anterior y el nuevo el mismo valor modificado
########################

dic7 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dic7.get("a")) #Solo obtine el valor de la Clave que indiquemos

#Dos forma de poder elimiar un par de valores dentro de un diccionario
dic8 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
del(dic8["a"]) #Elimina un par de valores especifico
print(dic8.pop("d")) #Aparte de poder modificar el nombre de una Clave tambien elimina un par de valor mediante la clave
print(dic8)

dic9 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic10 = {'c': 6, 'b': 5, 'e': 9, 'f': 10}
dic9.update(dic10) #Une los dos diccionario pero modifica del dic9 los registro que tengan la misma clave que del dic10
print(dic9)

print("Tambien se puede guardar listas dentro de los diccionarios de datos como vemos abajo")
#Tambien se puede guardar listas dentro de los diccionarios de datos como vemos abajo
diccionario1 = {
  "Luis": "Martinez",
  12: "Tres",
  32: 111,
  123: [1, "Film", 2.30, 19.0j]
}

print(diccionario1)

print(diccionario1[123][1])

diccionario1[123].extend(["Jorge"]) #Asi es como podemos agregar un dato a la lista dentro del diccionario
print(diccionario1)

diccionario1[123].extend("Jorge") #Si no encerramos el dato dentro de corchetes agregara por letra en la lista
print(diccionario1)

diccionario1[123][1] = "film" #Asi se modifica un dato de una lista dentro del diccionario
print(diccionario1)
