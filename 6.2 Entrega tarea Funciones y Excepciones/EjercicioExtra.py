'''Realiza una función que reciba una cadena de texto pedida al usuario por teclado 
y la imprima solo si es un palíndromo. La función se llamará espalindromo.'''

def espalindromo(word):
    if word != "":
        if str(word) == "".join(reversed(word)) :
            print("Es un palíndromo")
        else:
            print("No es un palíndromo")
    else:
        print("Cadena vacía!")

cadena = str(input("Introduzca una cadena de texto: "))
espalindromo(cadena) 
'''
espalindromo("ojo")
espalindromo("oj")
espalindromo("ojjjjjjjjjjjjjjjjjjjjo")
espalindromo("7777777777")
espalindromo("77777777778")
'''