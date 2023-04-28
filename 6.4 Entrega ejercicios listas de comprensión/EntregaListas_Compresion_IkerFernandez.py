'''
Dadas las listas x y personas

x = [8, 2, 3, 1, 2, 5, 7]

personas = ["Sara", "Pedro", "Miguel"]

1. Muestra el cubo de cada elemento de la lista x

2. Mostrar el cuadrado de los elementos impares de x

3. El cuadrado de los elementos pares y positivos de x

4. Los elementos de personas con más de 5 caracteres.

5. Los elementos de personas que contienen la vocal “o”.

6. Los elementos de personas que contienen la vocal “e” y además tienen una longitud de al menos 6 caracteres.'''

import re


x = [-2, 8, 2, 3, 1, 2, 5, 7]

personas = ["Sara", "Pedro", "Miguel"]

print("Introduce una de las siguientes opciones:\n\t1. Muestra el cubo de cada elemento de la lista x\n\t2. Mostrar el cuadrado de los elementos impares de x\n\t3. El cuadrado de los elementos pares y positivos de x\n\t4. Los elementos de personas con más de 5 caracteres.\n\t5. Los elementos de personas que contienen la vocal 'o'.\n\t6. Los elementos de personas que contienen la vocal 'e' y además tienen una longitud de al menos 6 caracteres.\n\t7. Salir.")

while True:
    try:
        opcion = int(input("\nOpción: "))
        if opcion == 1:
            result = [y ** 3 for y in x]
            print(result)
        elif opcion == 2:
            result = [y ** 2 for y in x if y % 2 != 0]
            print(result)
        elif opcion == 3:
            result = [y ** 2 for y in x if y % 2 == 0 and y > 0]
            print(result)
        elif opcion == 4:
            result = [y for y in personas if len(y) > 5]
            print(result)
        elif opcion == 5:
            result = [y for y in personas if re.search('o', y)]
            print(result)
        elif opcion == 6:
            result = [y for y in personas if re.search('e', y) and len(y) >= 6]
            print(result)
        elif opcion == 7 or opcion == 0:
            print("Saliendo...")
            break
        else:
            print(
                "Opción no reconocida. Elige una de las opciones anteriores (1-7). Pulse '0' o '7' para salir.")
    except ValueError:
        print("ERROR: Introduce un valor numérico!")
    except KeyboardInterrupt:
        print("\nSaliendo...")
        break
