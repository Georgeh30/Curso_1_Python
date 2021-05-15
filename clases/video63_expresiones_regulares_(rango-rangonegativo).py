from re import findall

cadena = "0123456789 ghi abcdef -*+/.[¡¿"

print(findall("[a-d0-5]", cadena))  # Mostramos desde la letra a hasta la d si esta dentro de una cadena y desde el 0 al 5

print(findall("[^a-d0-5]", cadena))  # Muestra lo que no esta en estos dos rangos

print(findall("[\d]", cadena))  # Muestra todos los numero que encuentre en la cadena

print(findall("[\D]", cadena))  # Muestra todos lo que NO son numeros que encuentre en la cadena

print(findall("[\w]", cadena))  # Muestra todos los caracteres siempre y cuando NO sean simbolos o signos

print(findall("[\W]", cadena))  # Muestra todos los signos, simbolos y espacio en blanco dentro de la cadena de texto

print(findall("[\s]", cadena))  # Muestra todos los espacios en blanco dentro de la cadena de texto
