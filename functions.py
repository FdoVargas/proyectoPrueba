# Trabajo Colaborativo: "Mini Agenda de Contactos"
# Objetivo:
# Desarrollar una pequeña aplicación de consola en Python que funcione como una agenda de contactos. El objetivo es aplicar los conocimientos de programación estructurada (variables, constantes, tipos de datos, estructuras de control, funciones, etc.) y prácticas básicas de trabajo colaborativo con Git y GitHub.
# ________________________________________
# Requisitos del Proyecto
# La aplicación debe permitir al usuario:
# 1.	Agregar un contacto: nombre, teléfono, email.
# 2.	Listar contactos: mostrar todos los contactos guardados.
# 3.	Buscar un contacto por nombre.
# 4.	Eliminar un contacto.
# 5.	Salir del programa.
# Debe usarse un menú para navegar entre estas opciones.
# La estructura de datos puede ser una lista de diccionarios.
# ________________________________________
# Organización del Trabajo
# •	El repositorio debe ser creado por uno de los integrantes del grupo y compartido con los otros.
# •	Todos deben clonar el repositorio en su computadora local.
# •	Cada alumno trabajará en una rama propia (ejemplo: rama-juan, rama-maria, rama-carlos).
# •	Cada uno será responsable de una parte del programa:
# o	Alumno 1: Función para agregar y mostrar contactos.
# o	Alumno 2: Función para buscar y eliminar contactos.
# o	Alumno 3: Estructura del menú principal y control de flujo del programa.
 
import time, os
def agregar(lista):
        os.system("cls")
        nombre = ""
        tel    = ""
        email  = ""
        print("Agregar un contacto.")
        while len(nombre)<3:
            nombre = input("ingrese un nombre:")
        while len(tel)<9: 
            tel = input("Ingrese número telefónico de 9 dígitos")
        while '@' not in email or len(email)<5:
             email = input("Ingrese su email")
        lista.append((nombre, tel, email))
        print("Contacto agregado con éxito!")
        time.sleep(0.9)

def mostrar_contactos(lista):
    if len(lista)==0:
        print("No existen contactos en la lista")
    else:
        contador= 1
        for nombre, tel, email in lista:
            print(f"{contador+1}, Nombre:{nombre}, Telefono: {tel},Correo: {email}")
        
