#LAS TUPLAS PUEDEN SER USADAS PARA CUANDO NO QUIERA QUE SE MODIFIQUE ALGUN DATO ESPECIFICADO DESDE LA CREACION DEL MISMO

ejemplo = ([40, 2], "Cincuenta", 23, "Doce")
print(ejemplo[0])

ejemplo2 = ("solo un dato en la tupla",) #Si solo se quiere un elemento dentro de la tupla se debe poner una coma al final
                                         # para que la variable sea detectada como una tupla
print(ejemplo2, type(ejemplo2))