'''Crea una lista con todos los números pares que hay entre 0 y 100'''

lista = [numero for numero in range(0, 101) if numero % 2 == 0]
print(lista)

str1 = "Aprendo Python 3 en el año 2023"
digits = [char for char in str1 if char.isdigit()]
print(digits)


'''Dada la siguiente lista de nombres junto a su edad devuelve una lista con los nombres y edad de las personas mayores de edad'''
personas = [('Pedro', 33), ('Ana', 3), ('César', 13), ('Carla', 45)]
personas_mayores = [x for x in personas if x[1] >= 18]
print(personas_mayores)


'''Crear una lista de pares a partir de otra lista creada con las potencias de 2 de los primeros 10 números'''
lista_anidada = [numero for numero in
                 [numero**2 for numero in range(0, 11)]
                    if numero % 2 == 0]
print(lista_anidada)

'''
1. Muestra el cubo de cada elemento de la lista x
2. Mostrar el cuadrado de los elementos impares de x
3. El cuadrado de los elementos pares y positivos de x
4. Los elementos de personas con más de 5 caractes
5. Los elementos de personas que contienen la vocal "0"
6. Los elementos de peronsas que contienen la vocal "e" y además tienen una longitud de al menos 6 caracteres
'''
x = [8,2,3,1,2,5,7]
personas = ["Sara", "Pedro", "Miguel"]

print("Introduce una de las siguientes opciones:\n\t1. Muestra el cubo de cada elemento de la lista x\n\t2. Mostrar el cuadrado de los elementos impares de x\n\t3. El cuadrado de los elementos pares y positivos de x\n\t4. Los elementos de personas con más de 5 caractes\n\t5. Los elementos de personas que contienen la vocal '0'\n\t6. Los elementos de peronsas que contienen la vocal 'e' y además tienen una longitud de al menos 6 caracteres")

while True:
    opcion = input("\nOpción: ")
    
    if opcion == "0":
        print([numero for numero in
                 [numero**2 for numero in range(0, 11)]
                    if numero % 2 == 0])
    elif opcion == "1":
        pass
    elif opcion == "2":
        pass
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        pass
    else:
        print("Orden no reconocida. Introduce 0 para salir.")



