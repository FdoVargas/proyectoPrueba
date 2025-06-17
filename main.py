import os, time
from functions import *
flag = True
contactos = []
while True:
    os.system("cls")
    menu(contactos)
    try:
        opcion= int(input("Ingrese una opción:\n"))
        if opcion ==1:
            os.system("cls")
            agregar(contactos)
            os.system("Pause")
        elif opcion ==2:
            os.system("cls")
            mostrar_contactos(contactos)
            os.system("Pause")
        elif opcion ==3:
            print("Eliminar contacto")
        elif opcion ==4:
            print("")
        elif opcion ==5:
            salir(contactos)
            break
        else:
            print("Opción ingresada no es válida")


    except:
        print("Ingrese un valor numérico")
        continue