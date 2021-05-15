from time import time  # Modulo que sirve para obtener el tiempo de ejecucion

start_time = time()  # Tiempo inicial
try:
    numero = int(input("Ingrese un Numero: "))
except ValueError as e:
    print(e)
else:
    print("No hubo ningun error")
finally:
    print("Termino el proceso {0} segundos".format((time() - start_time)))  # Tiempo inicial menos el Tiempo final
