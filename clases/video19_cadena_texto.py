cadena = "Soy Jorge Alvarado"
cadena2 = "Docuemnto F.inal"
cadena3 = """
La triple comilla dentro
de una variable
nos sirve para dar 
saltos de linea a un texto
guardado dentro de una variable
y al imprimirla nos muestra la palabra
ya con estos saltos de linea
"""

print(cadena3)

#Se puede obtener la letra contando desde derecha a izquierda ejem: -9A-8l-7v-6a-5r-4a-3d-2o-1

letra = cadena[4] #Obtenemos la letra de la posicion 4
palabra = cadena[4: 9] # Obtenemos la palabra ejem: 0S1o2y3 4J5o6r7g8e9 = Jorge
derecha = cadena[6:] #Mostramos apartir de la posicion 6 todo lo que esta de lado derecho
izquierda = cadena[:6] #Mostramos hasta la posicion 6 todo lo que esta de lado izquierdo
ultimaletra = cadena[-1] #Obtenemos la ultima letra
ciertaposicion = cadena2[cadena2.index(".") + 1:]  # Obtenemos de la cadena2 a partir de indice donde esta "." y mostramos la posicion siguiente (1) del punto
print(letra, palabra, ultimaletra) #Imprimimos las dos variables
print(derecha)
print(izquierda)
print("Obtiene lo que esta despues del (.):", ciertaposicion)

minuscula = cadena.lower() #cambia todas las letras a minusculas
isminuscula = minuscula.islower() #para comprobar si son todas minusculas o no
print(minuscula, isminuscula)

MAYUSCULA = cadena.upper() #CAMBIA TODAS LAS LETRAS A MAYUSCULAS
ISMAYUSCULA = MAYUSCULA.isupper() #PARA COMPROBAR SI SON TODAS MAYUSCULAS O NO
print(MAYUSCULA, ISMAYUSCULA)

separacion = cadena.split(' ') #Separa la cadena por espacio o por un signo/letra/numero
print(separacion)
print(separacion[2]) #Obtiener una posicion de las palabras separadas

#Para Insertar datos en una cadena te texto
cadenanueva = "Format nos {} para insertar datos dentro de una cadena de texto, {}, 2, 3".format("SIRVE", 1)
print(cadenanueva)

cadenanueva = "Format nos {a} para insertar datos dentro de una cadena de texto, {b}, 2, 3".format(a="Sirve", b=11)
print(cadenanueva)
