# OPCIONS PARA IMPORTAR DATOS DE OTRO ARCHIVO QUE SE CONVIERTE EN MODULO AL MOMENTO DE IMPORTARLO
import clases.video50_1_import_modulo  # ADVERTENCIA: PYTHON NO PUEDE IMPORTAR MODULOS QUE TENGAN SIGNOS COMO #
import clases.video50_1_import_modulo as alias  # Acortamos la ubicacion del import con un alias mas corto
from clases.video50_1_import_modulo import super_heroes as sh, tirar_dado as td  # Importamos datos especificos dandoles un alias pero igual no es necesario el alias

print(clases.video50_1_import_modulo.m_k)  # Aqui mando a llamar la variable (m_k) que esta en una subcarpeta (clases) y en el archivo llamado video50_1_import_modulo

print(clases.video50_1_import_modulo.tirar_dado(6))  # Mandamos a llamar la funcion y le damos como parametro 6 de 6 lados de un dado

print(clases.video50_1_import_modulo.super_heroes[2])  # Accedemos a la posicion 2 dentro de la lista creada en otro archivo o modulo

print(alias.super_heroes[1])  # Accedemos al archivo o modulo pero ahora escribiento el alias puesto en la parte de importacion del modulo para acortar el nombre

print(sh[3])  # Accedemos al modulo especificando solo el dato que queremos importar solamente

print(td(6))  # Accedemos atra ves del alias puesto en el tercer import a la funcion tirar_dado que esta en el modulo importado