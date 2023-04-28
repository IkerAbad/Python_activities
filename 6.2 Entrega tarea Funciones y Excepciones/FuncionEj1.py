'''
Crea un programa que determine si un número es primo o no. Deberás crear la función esPrimo()
que reciba como parámetro un número y devuelva True o False indicando si el número es primo o
no.
'''

def esPrimo(n): 
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False

    return True

print(esPrimo(23))