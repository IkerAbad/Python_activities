class Alumno:
    def __init__(self, nombre, apellidos, edad, curso, clase):
        self.nombre= nombre
        self.apellidos = apellidos
        self.edad = edad
        self.curso = curso
        self.clase = clase
        
    def matricula(self):
        print("El alumno", self.nombre, self.apellidos, "de edad", self.edad, "se encuentra matriculado en el curso de", self.curso, ", clase", self.clase)
        
alumno1 = Alumno("Iker", "Fernández Antón", "22", "DAM", "31F")

alumno1.matricula()