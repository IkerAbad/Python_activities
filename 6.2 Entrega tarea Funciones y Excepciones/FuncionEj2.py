'''
Crea un programa que genere un número aleatorio del 1 al 10. El usuario tendrá que adivinarlo, y
el programa tras cada intento le indicará al usuario si el número es más alto, bajo o si ha acertado.
La lógica para dar la respuesta al usuario deberá estar incluida en una función a la que se llamará
tras cada intento.
Nota: Para la creación del número aleatorio, utiliza el siguiente código:
1 from random import randint, uniform,random
2
3 numero = randint(0,10)'''
from random import randint

def jugar(n,g):
    if n != g:
        if n < g:
            print("Es un número mayor a", n)
            return False
        else:
            print("Es un número menor a", n)
            return False
    else:
        print("Número correcto!")
        return True
    
guess = int(randint(0,10))
#guess = 5
print("Se ha generado un número del 1 al 10.")
num = int(input("Introduce números hasta adivinarlo: "))

while True:
    if jugar (num,guess):
        break
    else:
        num = int(input("Introduce otro número: "))


