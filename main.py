import os, time
from functions import *

contactos = []
print("""
        Agenda contactos
1.	Agregar un contacto: nombre, teléfono, email.
2.	Listar contactos: mostrar todos los contactos guardados.
3.	Buscar un contacto por nombre.
4.	Eliminar un contacto.
5.	Salir del programa.""")
try:
    opcion= int(input("Ingrese una opción"))
    if opcion ==1:
        os.system("cls")
        agregar(contactos)
        os.system("Pause")
    elif opcion ==2:
        print("Lista de contactos")
    elif opcion ==3:
        print("Eliminar contacto")
    elif opcion ==4:
        print("")
    elif opcion ==5:
        print("")
    else:
        print("Opción ingresada no es válida")


except:
    print("Ingrese un valor numérico")