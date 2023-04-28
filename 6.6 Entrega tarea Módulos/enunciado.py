'''
1. Crea un módulo llamado areas.txt: debe tener la variable pi con un valor de 3.141592
la función cuadrado que debe calcular el área del cuadrado en función de su lado. Se le pasará el lado como parámetro y devolverá su cuadrado. La función circulo calcula el área del circulo a partir del a partir del radio. (pi x radio ^2). Añade al módulo dos instrucciones. Documenta el módulo con las siguientes cadenas de texto:
y comprueba que funcionan:
Módulo: módulo de áreas básicas.
Cuadrado: Calcula el área del cuadrado a partir de su lado
Circulo: Calcula el área del circulo dado el radio

2. Importar el módulo del ejercicio anterior para que se ejecuten las instrucciones sin errores:
a, b = 11, 3
print (‘operandos = ‘, a,b)
print ('Area cuadrado =', areas.cuadrado(a))
print ('Area circulo =', areas.circulo(b))

¿Cómo debería importar el módulo para que no hubiera errores al ejecutar?
a, b = 11, 3
print (‘operandos = ‘, a,b)
print ('Area cuadrado =', ld.cuadrado(a))
print ('Area circulo =', ld.circulo(b))

3. ¿Cómo importaría para que funcionara el código siguiente?
a, b = 11, 3
print (‘operandos = ‘, a,b)
print ('Area cuadrado =', cuadrado(a))

print ('Area circulo =', circulo(b))

4. Muestra la documentación del módulo.

5. Modifica el ejemplo de la página 61 para que la función dividir lance una excepción en caso de división por cero. El código de esa excepción mostrará el mensaje 'ERROR: No se puede dividir por cero' y lanzará una excepción del tipo ZeroDivisionError
'''