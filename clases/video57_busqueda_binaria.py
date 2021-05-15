# Busqueda a través de sumas y divisiones de los indices

lista = [5, 6, 12, 67, 34, 98, 43, 1, 23, 0, 87, 32, 45, 60, 2, 167]  # Debemos ordenar la lista en primer lugar
lista.sort()  # La ordenamos con el metodo sort()
print(lista)  # La imprimimos solo para confirmar que este ordenada


# Hacemos la funcion que nos retornara la posicion donde se encuentra el valor en la lista ya ordenada
def busqueda_binaria(dato):
    inicio = 0
    final = len(lista) - 1
    while inicio <= final:
        puntero = (inicio + final) // 2
        if dato == lista[puntero]:
            return str(input(f"El numero {dato} se encuentra en la posicion {puntero}\nPRESIONE ENTER PARA CONTINUAR"))
        elif dato > lista[puntero]:
            inicio = puntero + 1
        else:
            final = puntero - 1
    return str(input(f"El numero {dato} no se encontro\nPRESIONE ENTER PARA CONTINUAR"))


while True:
    print("************MENÚ************")
    opciones = input("1. Buscar"
                     "\n2. Salir"
                     "\nSeleccione una Opcion: ")

    if opciones == "1":
        print(busqueda_binaria(int(input("Ingrese el Valor a Buscar: "))))  # Mandamos a llamar la funcion para buscar
    if opciones == "2":
        print("Has Terminado!!")
        break
