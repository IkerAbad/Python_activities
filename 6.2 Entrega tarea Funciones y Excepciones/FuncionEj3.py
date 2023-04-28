'''
Crea un programa que reciba un número del 1 al 20 introducido por el usuario y compruebe si está
dentro de la siguiente lista: [6,14,11,3,2,1,15,19]. Implementa una función que se asegure que el
número introducido por el usuario está en el rango indicado y otra que compruebe si está dentro
de la lista. Trata de crear las funciones de forma que puedan ser reutilizadas lo máximo posible en
otros programas.'''

lista = [6,14,11,3,2,1,15,19]

def rango(n):
    if n < 1 or n > 20:
        print("Número no válido! Tiene que ser un número del 1 al 20.")
        return False
    else:
        return True
    
def comprobar(n):
    if n in lista:
        print("El número", n, "se encuentra en la lista", lista)
        return True
    else:
        print("El número", n, "no se encuentra en la lista", lista)
        return False

while True:
    num = int(input("Introduce un número del 1 al 20: "))
    if rango(num):
        if comprobar(num):
            break
        else:
            break
            

