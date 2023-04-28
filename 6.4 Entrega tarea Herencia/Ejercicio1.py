'''
Ejercicio 1
Continuando con el Ejercicio 1 del tema anterior, crea una clase Vehículo y otra llamada Bicicleta.
La clase Vehículo será el padré de Coche y Bicicleta y contendrá las propiedades y/o métodos
comunes de ambos. La bicicleta no tendrá gasolina ni repostará, pero cada 50 kilometros necesitará
invocar al método hinchar_ruedas() o no podrá continuar.
Puedes utilizar este código para comprobar que todo funciona correctamente:
1 # Coche:
2 coche = Coche("1122PKL","Audi")
3 coche.repostar(20)
4 coche.avanzar(120)
5 print(f"Total de kms coche: {coche.kilometros}. Gasolina: {coche.gasolina}")
6 coche.avanzar(40)
7 print(f"Total de kms coche: {coche.kilometros}. Gasolina: {coche.gasolina}")
8
9 # Bicicleta
10 bicicleta = Bicicleta("BH")
11 bicicleta.avanzar(30)
12 print(f"Total de kms bici: {bicicleta.kilometros}")
13 bicicleta.avanzar(25)
14 print(f"Total de kms bici: {bicicleta.kilometros}")
15 bicicleta.hinchar_ruedas()
16 bicicleta.avanzar(25)
17 print(f"Total de kms bici: {bicicleta.kilometros}")

Resultado:

Herencia
1 Total de kms coche: 120. Gasolina: 8.0
2 Total de kms coche: 160. Gasolina: 4.0
3
4 Total de kms bici: 30
5 Es necesario hinchar para recorrer la cantidad indicada de kms.
6 Total de kms bici: 30
7 Total de kms bici: 55'''

class Vehiculo:
    def __init__(self) -> None:
        pass
    
class Bicicleta:
    def __init__(self) -> None:
        pass