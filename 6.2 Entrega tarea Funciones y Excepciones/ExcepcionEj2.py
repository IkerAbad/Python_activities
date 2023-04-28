'''
Crea una aplicación reciba la clave de un diccionario y acceda a uno de sus valores. Asegúrate de que
capturas las excepciones que puedan saltar al intentar acceder a una clave del diccionario inexistente.'''

dicc={1:"esto", 2:"es", 3:"python"}

print("Introduzca un número que indique una clave en el siguiente diccionario: {'1':'esto', '2':'es', '3':'python'}")
while True:
    try:
        num = int(input("Posición: "))
        print(dicc[num])
        break
    except ValueError:
        print("ERROR: Tiene que introducir un número entero.")
    except KeyError:
        print("ERROR: No existe esa clave en el diccionario.")

    