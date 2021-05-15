i = 1

while i <= 5:
    print(i)
    i += 1

dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miercoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sabado",
    7: "Domingo"
}

#OPCION UNO PARA IMPRIMIR CLAVE O VALOR O LOS DOS A LA VEZ
for dia in dias:
    print(dia, ":", dias[dia])

#OPCION DOS PARA IMPRIMIR CLAVE O VALOR O LOS DOS A LA VEZ
for clave, dia in dias.items():
    print(clave, ":", dia)

print("\n")

#Esta forma es para indicar que imprima empezando por el 0 en uno en uno siempre
# y cuando sea menor o igual al rango 6
for indice in range(6):
    print(indice)

print("\n")

#Aqui le indicamos que imprima desde el rango 3 al 8, recordando que empieza
# desde cero los numero que imprime
for indice2 in range(3, 8):
    print(indice2)

print("\n")

for indice3 in range(3, 8, 2): #aqui indicamos desde (donde empeza, donde termina, cada cuando imprime los valores(osea en uno en uno o en dos en dos y asi..))
    print(indice3)

print("\n")

dias2 = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"] #Este es una Lista

for indice123 in range(len(dias2)):
    print(dias2[indice123])