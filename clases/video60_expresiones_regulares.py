from re import search, findall, split, sub

cadena = "Esto es una Cadena de Texto, Esto es una Cadena de Texto"

'''
print(search("Cadena", cadena))  # Devuelve la posicion inicial y final donde se ubica la primera palabra que la encuentra, si no la encuentra devuelve None

buscar = search("Cadena", cadena)

print(buscar.group())  # Devuelve la palabra que buscamos
print(buscar.start())  # Devuelve la posicion inicial donde encontro la cadena
print(buscar.end())  # Devuelve la posicion final donde encontro la cadena
print(buscar.span())  # Devuelve la posicion inicial y final de la ubicacion de la cadena
print(buscar.string())
'''

palabra_encontrada = findall("Texto", cadena)

print(palabra_encontrada)  # Devuelve una lista con todas las coincidencias la cadena a buscar
print(len(palabra_encontrada))  # Devuelve el numero de veces que encuentra una cadena o palabra

cadena_separada = split(" ", cadena)  # Devuelve la cadena de texto separada por lo que asignamos dentro de las comillas

print(cadena_separada)  # Mostramos la lista donde esta la cadena separada en este caso por el espacio

reemplazador_palabras = sub("Cadena", "Secuencia", cadena)  #Devuelve la cadena reemplazando la primera palabra que
                                                            # buscamos "Cadena" dentro de ella por la segunda palabra escrita "Secuencia"

print(reemplazador_palabras)  # Muestra la cadena de texto ya con las palabras reemplazadas
