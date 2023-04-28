#Author     Iker Fernández Antón
'''
Realiza los siguientes ejercicios en Python:

Dados los ficheros "datos.txt" que debes crear en el ejercicio 2 y "comentarios.txt" que es un fichero que debe contener unas líneas comentadas (al principio) y otras no.

++1. Guardar en otro fichero que tú quieras de texto una línea con la operación de suma que incluya todos los operandos y el resultado. P.ej. 24 + 34 + 2 = 60
++2. Añadir la línea [1,2,3,4, . . . . 10] a datos.txt (No sobre escribas si es que tiene datos) 
++3. Muestra el producto de los números de la última línea de datos.txt
++4. El número de líneas del fichero "comentarios.txt" si ignoramos las comentadas (comienzan por #). Puede ser de gran ayuda el método startswith. 
++5. La suma de todos los números impares de datos.txt. 
'''
import re
import math

print("Introduce una de las siguientes opciones:\n\t1. Guardar en un fichero de texto una línea con la operación de suma que incluya todos los operandos y el resultado.\n\t2. Añadir líneas al archivo 'datos.txt'.\n\t3. Muestra el producto de los números de la última línea de 'datos.txt'.\n\t4. El número de líneas del fichero 'comentarios.txt' (ignorando comentarios).\n\t5. Suma todos los números impares de 'datos.txt'.\n\t6. Salir.")


while True:
    try:
        option = int(input("\nOpción: "))
        sum = 0
        line = ""
        result = []
        if option == 1:
            file = open(
                "./6.5 Entrega tarea ficheros en Python/comentarios.txt", "a+")
            num = int(
                input("Introduce, uno a uno, los números que quieras sumar: "))
            if num != 0:
                file.write('\n' + str(num))
                while True:
                    sum = sum + int(num)
                    if int(num) == 0:
                        file.write(' = ' + str(sum))
                        break
                    else:
                        num = input(
                            "Introduce otro número ('0' para salir e imprimir la suma): ")
                        if num != '0':
                            file.write(' + ' + str(num))
            print("Resultado de la suma =", sum)
            file.close()

        elif option == 2:
            file = open(
                "./6.5 Entrega tarea ficheros en Python/datos.txt", "a+")
            line = str(
                input("Introduce una línea para añadir al documento: "))
            file.write(str(line))
            while True:
                option = str(input("¿Quiere añadir otra línea? (Sí/No): "))
                if option == "Sí" or option == "sí" or option == "SÍ" or option == "sÍ" or option == "si" or option == "Si" or option == "sI" or option == "SI":
                    line = str(
                        input("Introduce una línea para añadir al documento: "))
                    file.write('\n' + str(line))
                elif option == "No" or option == "nO" or option == "no" or option == "NO":
                    break
                else:
                    print("ERROR: Orden no reconocida. Introduzca 'Sí' o 'No'")
            file.close()

        elif option == 3:
            try:
                with open("./6.5 Entrega tarea ficheros en Python/datos.txt") as f:
                    for line in f:
                        pass
                    last_line = line
                    result = re.split('[+=]', last_line)
                    result = [x.strip(' ') for x in result]
                    product = 1
                    for num in result:
                        product = product * int(num)
                    print(product)
            except ValueError:
                print(
                    "ERROR: En la última línea del archivo 'datos.txt' no se encuentran valores números para multiplicar...")

        elif option == 4:
            file = open(
                "./6.5 Entrega tarea ficheros en Python/comentarios.txt", "r")
            for line in file.readlines():
                if line.startswith('#'):
                    pass
                else:
                    sum = sum + 1
            print("Número total de líneas:", sum)
            file.close()

        elif option == 5:
            file = open(
                "./6.5 Entrega tarea ficheros en Python/datos.txt", "r")
            for line in file:
                result.append(line.split())
            for line in result:     
                for i in line:
                    if i.isdigit():
                        if int(i) % 2 != 0:
                            sum = int(i) + int(sum)
            print("Suma de todos los números impares en 'datos.txt':", sum)
            file.close()

        elif option == 6 or option == 0:
            print("Saliendo...")
            break
        else:
            print(
                "Opción no reconocida. Elige una de las opciones anteriores (1-6). Pulse '0' o '6' para salir.")
    except ValueError:
        print("\nERROR: Introduce un valor numérico!")
    except KeyboardInterrupt:
        print("\nSaliendo...")
        break
    except FileNotFoundError:
        print("\nERROR: El archivo no existe!")
    except AttributeError:
        print("\nERROR: Este atributo no existe!")
