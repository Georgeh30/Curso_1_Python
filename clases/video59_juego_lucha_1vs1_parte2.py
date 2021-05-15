from clases.video59_juego_lucha_1vs1 import Animal
from random import randint


def juego(p1=Animal, p2=Animal):
    turno = randint(1, 2)

    while True:
        if p1.vida > 0 and p2.vida > 0:
            if turno == 1:
                print(str(input(f"Es el Turno del Animal {p1.nombre}\nPRESIONE ENTER PARA ATACAR")))
                p2.vida = p2.vida - p1.ataque
                print(f"Vida de {p2.nombre}: " + str(p2.vida))
                turno = 2
            else:
                print(str(input(f"Es el Turno del Animal {p2.nombre}\nPRESIONE ENTER PARA ATACAR")))
                p1.vida = p1.vida - p2.ataque
                print(f"Vida de {p1.nombre}: " + str(p1.vida))
                turno = 1
        else:
            if p1.vida <= 0:
                print(p2.gano())
                print(str(input("PRESIONE ENTER PARA CONTINUAR")))
                break
            else:
                print(p1.gano())
                print(str(input("PRESIONE ENTER PARA CONTINUAR")))
                break


while True:
    print("************MENÚ************")
    opciones = input("1. Empezar el juego"
                     "\n2. Salir"
                     "\nSeleccione una Opcion: ")

    print()  # Solo para dar salto de linea

    if opciones == "1":
        juego(p1=Animal(str(input("Jugador 1 --> Nombre: ")), int(input("Jugador 1 --> Vida: "))), p2=Animal(str(input("Jugador 2 --> Nombre: ")), int(input("Jugador 2 --> Vida: "))))  # Mandamos a llamar la funcion
        print()  # Solo para dar salto de linea
    if opciones == "2":
        print("Has Terminado!!")
        break
