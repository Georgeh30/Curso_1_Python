import re

correo = 'nombre@dominio.com'

if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', correo.lower()):
    print("Correo correcto")
else:
    print("Correo incorrecto")
