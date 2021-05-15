# El break puede funcionar para detener un ciclo dentro de ...
# el o para hacer que salte un dato y siga continuando el ciclo

diccionario = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo"}

for obtengo in diccionario:
    print(obtengo)
    if obtengo == 3:
        break

print("\n")

for obtengo2 in diccionario:
    if obtengo2 == 3:
        continue
    print(obtengo2)