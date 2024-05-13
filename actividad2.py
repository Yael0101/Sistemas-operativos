Python 3.11.6 (main, Oct  8 2023, 05:06:43) [GCC 13.2.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Autor Jesus Yael Arellano Limon
... import subprocess
... 
... def menu():
...     print("1. Crear archivo misnotas.txt")
...     print("2. Crear carpeta calificaciones")
...     print("3. Crear carpeta primer parcial")
...     print("4. Mover archivo misnotas.txt a carpeta calificaciones")
...     print("5. Mover programa calculadora.py a carpeta primer parcial")
...     print("0. Salir")
... 
... while True:
...     menu()
...     opcion = input("Seleccione una opción: ")
... 
...     if opcion == "1":
...         subprocess.run("touch misnotas.txt", shell=True)
...     elif opcion == "2":
...         subprocess.run("mkdir calificaciones",shell=True)
...     elif opcion == "3":
...         subprocess.run("mkdir calificaciones/primerparcial", shell=True)
...     elif opcion == "4":
...         subprocess.run("mv misnotas.txt calificaciones/", shell=True)
...     elif opcion == "5":
...         subprocess.run("mv calculadora.py calificaciones/primerparcial/",shell=True)
...     elif opcion == "0":
...         break
...     else:
