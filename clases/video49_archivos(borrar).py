# Archivos de texto u otro tipo de archivo
import os

#Borrar
try:
    os.remove("nuevo.txt")
except FileNotFoundError as e:
    print(e)