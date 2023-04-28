'''
Crea un programa que acceda a la posición que el usuario indique de la siguiente lista: [6,14,11,3,2,1,15,19].
No olvides capturar las excepciones que puedan surgir en caso de que el usuario introduzca un índice
incorrecto o que no exista en la lista.
'''
lista = [6,14,11,3,2,1,15,19]

print("Introduzca un número que indique una posición en la siguiente lista: [6,14,11,3,2,1,15,19]")
while True:
    try:
        num = int(input("Posición: "))
        print(lista[num])
        break
    except ValueError:
        print("ERROR: Tiene que introducir un número entero.")
    except IndexError:
        print("ERROR: No existe esa posición en la lista.")

    