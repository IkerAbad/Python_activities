'''
Crea la clase Coche que contenga las siguientes propiedades:
• matrícula (string)
• marca (string)
• kilometros_recorridos (float)
• gasolina (float)
La clase tendrá un método llamado avanzar() que recibirá como argumento el número de kilómetros
a conducir y sumará los kilómetros recorridos al valor de la propiedad kilometros_recorridos. El
método también restará al valor de gasolina el resultado de los kilómetros multiplicado por 0’1.
La clase también contendrá otro método llamado repostar() que recibirá como argumento los litros
introducidos que deberán sumarse a la variable gasolina.
Por último, será necesario controlar que el método avanzar nunca obtendrá un número negativo en
la gasolina. En dicho caso, deberá mostrar el siguiente mensaje: “Es necesario repostar para recorrer
la cantidad indicada de kilómetros”.
Ejemplo:
- avanzar(50) # gasolina = 50
- avanzar(100) # kilometros_recorridos = 100, gasolina = 40
- avanzar(40) # kilometros_recorridos = 140, gasolina = 36
- avanzar(180) # kilometros_recorridos = 320, gasolina = 18'''


class Coche:
    def __init__(self, matricula, marca, kilometros_recorridos, gasolina):
        self._matricula = str(matricula)
        self._marca = str(marca)
        self._kilometros_recorridos = float(kilometros_recorridos)
        self._gasolina = float(gasolina)

    def avanzar(self, km):
        self._kilometros_recorridos = self._kilometros_recorridos + km
        print("Kilómetros:", self._kilometros_recorridos)
        if self._gasolina > 0.00:
            self._gasolina = self._gasolina - \
                (self._kilometros_recorridos * 0.1)
            print("Gasolina:", self._gasolina)
        else:
            print(
                "Es necesario repostar para recorrer la cantidad indicada de kilómetros")

    def repostar(self, litros):
        self._gasolina = self._gasolina + litros


coche1 = Coche("m101010", "BMW", "100", "40")

coche1.avanzar(50)

coche1
