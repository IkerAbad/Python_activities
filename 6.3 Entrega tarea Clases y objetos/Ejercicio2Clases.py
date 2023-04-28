'''
Crea una clase Robot que simule los movimientos de un robot y calcule la posición en la que se
encuentra cada momento. El robot se moverá por un tablero infinito de coordenadas X e Y, podrá
realizar los siguientes movimientos:
• Avanzar hacia adelante (A)
• Retroceder (R)
• Avanzar hacia la izquierda (I) o hacia la derecha (D)

Clases y objetos 43
El robot tendrá un método llamado mueve() que recibirá la orden como parámetro y otro método,
posicion_actual(), que indicará su posición en las coordenadas X e Y. Al crear el robot este se
inicializará a las coordenadas (0,0).
Puedes utilizar el siguiente código para probar la clase creada:
1 miRobot = Robot()
2 orden = "A"
3 while orden != 'fin':
4 orden = input("Introduce la orden: ")
5 miRobot.mueve(orden)
6 print(miRobot.posicion_actual())
Ejemplo:
1 >> Introduce la orden: A
2 Posición actual: 1,0
3 >> Introduce la orden: A
4 Posición actual: 2,0
5 >> Introduce la orden: I
6 Posición actual: 2,-1
7 >> Introduce la orden: A
8 Posición actual: 3,-1
9 >> Introduce la orden: I
10 Posición actual: 3,-2
11 >> Introduce la orden: D
12 Posición actual: 3,-1
13 >> Introduce la orden: R
14 Posición actual: 2,-1
15 >> Introduce la orden: fin
'''


class Robot:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def mueve(self, mov):
        mov = mov.upper()
        if mov == "A":
            self.y = self.y + 1
        elif mov == "R":
            self.y = self.y - 1
        elif mov == "I":
            self.x = self.x - 1
        elif mov == "D":
            self.x = self.x + 1
        else:
            print("Orden no reconocida. (A, R, I, D) Para desplazarte. Introduce 'fin' para salir.")

    def posicionactual(self):
        print(">> Posición actual:", self.x, ",", self.y)

miRobot = Robot()
orden = ""

while orden != 'fin':
    orden = input("Introduce la orden: ")
    miRobot.mueve(orden)
    miRobot.posicionactual()
    
