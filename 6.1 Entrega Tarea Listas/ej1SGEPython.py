'''
Dada la siguiente lista [12, 23, 5, 29, 92, 64] realiza las siguientes operaciones y vete mostrando
la lista resultante por pantalla:
1. Elimina el último número y añádelo al principio.
2. Mueve el segundo elemento a la última posición.
3. Añade el número 14 al comienzo de la lista.
4. Suma todos los números de la lista y añade el resultado al final de la lista.
5. Fusiona la lista actual con la siguiente: [4, 11, 32]
6. Elimina todos los números impares de la lista.
7. Ordena los números de la lista de forma ascendente.
8. Vacía la lista.
'''

lista = [12, 23, 5, 29, 92, 64]
lista2 = [4, 11, 32]

while True:

    print ("Con la lista:", lista)
    print("Elija una de las siguientes opciones:\n\t1. Elimina el último número y añádelo al principio.\n\t2. Mueve el segundo elemento a la última posición.\n\t3. Añade el número 14 al comienzo de la lista.\n\t4. Suma todos los números de la lista y añade el resultado al final de la lista.\n\t5. Fusiona la lista actual con la siguiente: [4, 11, 32]\n\t6. Elimina todos los números impares de la lista.\n\t7. Ordena los números de la lista de forma ascendente.\n\t8. Vacía la lista.\n\t9. Salir del programa.")
    opcion = input("\nOpción: ")

    if opcion == "1":
        num = lista [-1]
        lista.pop()
        lista.insert(0,num)
    elif opcion == "2":
        num = lista [1]
        lista.pop(1)
        lista.append(num)
    elif opcion == "3":
        lista.insert(0,14)
    elif opcion == "4":
        num = 0
        for x in lista:
            num = num + x
        lista.append(num)
    elif opcion == "5":
        lista = lista + lista2
    elif opcion == "6":
        rem = []
        for x in lista:
            if x % 2 !=0:
                rem.append(x)
        for x in rem:
            for i in lista:
                if x == i:
                    lista.remove(i)
    elif opcion == "7":
        lista.sort()
    elif opcion == "8":
        lista.clear()
    elif opcion == "9":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no disponible")