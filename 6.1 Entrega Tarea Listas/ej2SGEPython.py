'''
Crea un programa que solicite al usuario 5 números y los guarde en una lista. A continuación el
programa pedirá otros 5 números al usuario almacenándolos en una segunda lista. El programa
mostrará al usuario una lista que contenga los números que tienen en común las dos listas anteriores.
• Ejemplo: Lista 1 = [6,14,11,78,5] y Lista 2 = [3,14,22,78,9]
• Resultado: [14, 78]'''

print("Introduce 5 números")
n1 = input("Primer número: ")
n2 = input("Segundo número: ")
n3 = input("Tercer número: ")
n4 = input("Cuarto número: ")
n5 = input("Quinto número: ")
lista1 = [n1,n2,n3,n4,n5]
print("Introduce otros 5 números")
n1 = input("Primer número: ")
n2 = input("Segundo número: ")
n3 = input("Tercer número: ")
n4 = input("Cuarto número: ")
n5 = input("Quinto número: ")
lista2 = [n1,n2,n3,n4,n5]
repetidos = []
for x in lista1:
    for i in lista2:
        if x == i:
            repetidos.append(i)
            
print("Números repetidos:",repetidos)

