'''
Continuando con el Ejercicio 4 del tema anterior, crea una clase Poligono y otra llamada Cuadrado.
La clase Poligono será el padre de Triangulo y Cuadrado, y contendrá las propiedades y métodos
comunes de ambos. Ambos tendrán también otra propiedad llamada color.
1 t1 = Triangulo("rojo",[2, 5, 2])
2 print(f" Es un {t1.forma()} {t1.color} con {t1.perimetro()}m de perímetro.")
3
4 c1 = Cuadrado("azul",[4, 4, 4, 4])
5 print(f" Cuadrado {c1.color} con {c1.perimetro()}m de perímetro.")
Resultado:
1 Es un Triángulo isósceles rojo con 9m de perímetro.
2 Cuadrado azul con 16m de perímetro.'''