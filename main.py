import os
import time
from functions import *

contactos = []
print("""
        Agenda contactos
1.	Agregar un contacto: nombre, teléfono, email.
2.	Listar contactos: mostrar todos los contactos guardados.
3.	Buscar un contacto por nombre.
4.	Eliminar un contacto.
5.	Salir del programa.""")
while True:
    try:
        opcion = int(input("Ingrese una opción"))
        if opcion == 1:
            os.system("cls")
            agregar(contactos)
            os.system("Pause")
        elif opcion == 2:
            # os.system("cls")
            mostrar_contactos(contactos)
            os.system("Pause")
        elif opcion == 3:
            buscar_contacto(contactos)
        elif opcion == 4:
            eliminar_contacto(contactos)
        elif opcion == 5:
            print("Saliste del programa :) ")
        else:
            print("Opción ingresada no es válida")

    except:
        print("Ingrese un valor numérico")
