#Son igual que las listas, tuplas o diccionario, pero este no ordena los datos que guardas dentro de el
# y los datos repetidos no los agrega

conjunto = {"Jorge", True, "+", 123, 11.23, 44.0j}

print(conjunto) #muestra los datos de otra forma desordenada

conjunto.add("Jorge") #Si se agrega el mismo dato que ya hay dentro, no lo guarda

print(conjunto)
