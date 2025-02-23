import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y  # Aquí asignamos y a self.y

    def coord_cartesianas(self):
        return self.x, self.y

    def coord_polares(self):
        radio = math.sqrt(self.x * self.x + self.y * self.y)
        angulo = math.atan2(self.y, self.x)
        angulo = math.degrees(angulo)
        return radio, angulo

    def __str__(self):
        return "({:.2f},{:.2f})".format(self.x, self.y)

class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Línea desde {self.p1} hasta {self.p2}"

    def dibujaLinea(self):
        return f"Dibujando línea desde {self.p1} hasta {self.p2}"

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def __str__(self):
        return f"Círculo con centro en {self.centro} y radio de {self.radio:.2f}"

    def dibujaCirculo(self):
        return f"Dibujando círculo con centro en {self.centro} y radio de {self.radio:.2f}"

# Ejemplo de uso:
p1 = Punto(0, 3)
p2 = Punto(3, 4)
linea = Linea(p1, p2)
circulo = Circulo(p1, 5)

print(linea)
print(linea.dibujaLinea())
print(circulo)
print(circulo.dibujaCirculo())
