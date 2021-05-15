# NOTA: .lower() --> cambia temporalmente la letra o frase a minuscula pero NO la guarda como minuscula
#       .isupper() --> detecta si es Mayuscula la letra o palabra
#       .upper() --> convierte a Mayuscula la letra o palabra


def encriptador(frase, caracter):
    encriptada = ""
    for letra in frase:  # Guardamos la letra de la frase
        if letra.lower() in "aeiouáéíóú":  # Si la letra convertida a minuscula (letra.lower()) se encuentra en la cadena de caracteres (aeiouáéíóú) entra y...
            if letra.isupper():  # Si la letra esta en Mayuscula
                encriptada = encriptada + caracter.upper()  # Guardamos el caracter convertido a Mayuscula (caracter.upper()) mas el caracter que este en la variable (encriptada)
            else:  # Si no esta en Mayuscula la letra
                encriptada = encriptada + caracter  # Guardamos el caracter en minuscula mas el caracter que tenga la variable (encriptada) actualmente
        else:  # Si no se encuentra la letra dentro de la cadena de caracteres (aeiouáéíóú)
            encriptada = encriptada + letra  # Guardamos el caracter (letra) mas la actual (encriptada)
    return encriptada  # Retornamos el valor ya unido


print(encriptador(input("Ingresa una frase:\n>"), "x"))  # Mandamos a llamar la funcion