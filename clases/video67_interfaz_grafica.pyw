""" NOTA IMPORTANTE: (AL CAMBIAR LA EXTENCION .py A .pyw PODEMOS EJECUTAR ESTE ARCHIVO DESDE DOCUMENTOS CON DOBLE CLIC
    COMO UNA APLICACION, OSEA QUE PODEMOS ABRIR LA VENTANA CREADA)"""

import ctypes  # Modulo para cambiar el icono de la ventana por el icono personalizado
from tkinter import *  # Modulo para la interfaz grafica


"""ESTAS DOS LINEAS DE CODIGO SON PARA QUE SE CAMBIE EL ICONO DE LA VENTANA EN LA BARRA DE TAREAS"""
myappid = 'empresa.appnombre.servicio.version1'  # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
"""FIN DE ESTE CODIGO DE CAMBIO DE ICONO EN LA BARRA DE TAREAS"""


root = Tk()  # Creamos la instancia raiz o root de tkinder y la guardamos en la variable que llamamos root

root.title("Ventana Nueva")  # Ponemos un titulo de ventana
root.geometry("600x300+0+0")  # Asinamos el ancho y el alto de la ventana
root.config(
    bg="#2b2b2b"  # Para cambiar el color de fondo de la ventana
)
#root.resizable(False, False)  # Damos permisos de redimenzionar la ventana o de no redimenzionar
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))  # Ayuda a Centrar la ventana

""" NOTA: Poner hasta el final de las configuracions de la instancia raiz o root Tk(), 
    para no tener errores o incongruencias"""
root.iconbitmap("icono.ico")  # Ponemos un icono de ventana personalizado

# CREACION DEL FRAME O CUADRO
frame = Frame(root)  # Creamos un frame o cuadro hijo de la raiz o root

# Empaquetamos el frame o cuadro dentro de la raiz
frame.pack(
    # side=RIGHT,  # Para mantener el frame siempre a la derecha del root
    # anchor=CENTER,  # Para mantener siempre centrado
    fill="both",  # REDIMENSIONAMOS EL FRAME AL TAMAÑO DEL ROOT
    expand=1  # PONEMOS 1 O TRUE INDICANDO QUE AUTORIZE E¿LA EXPANCION DEL FRAME
)

frame.config(
    bg="White",  # Cambiamos el color del frame o cuadro
    width=600,  # Asignamos el ancho
    height=300,  # Asignamos la altura
    cursor="pirate",  # Cambiar el cursor cuando este dentro del frame
    relief="groove",  # Damos un borde con un estilo especifico
    bd=20  # Y su ancho del borde
)

root.mainloop()  # Esta linea de codigo debe de ir siempre al final, realiza un ciclo infinito para detectar cualquier peticion dentro de la ventana
