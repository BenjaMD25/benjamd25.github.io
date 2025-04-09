import numpy as np
import matplotlib.pyplot as plt

class Punto2D:
    def __init__(self, x=0, y=0):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x = x
            self.y = y
        else:
            raise ValueError('Error, solo se pueden ingresar valores reales')
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __call__(self, a):
        return Punto2D(self.x * a, self.y * a)
    def __add__(self, other):
        return Punto2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Punto2D(self.x - other.x, self.y - other.y)
    def __rmul__(self, other):
        return Punto2D(self.x * other, self.y * other)
    def __abs__(self):
        return float(np.sqrt(self.x**2 + self.y**2))
    def graficar(self):
        plt.plot(self.x, self.y, 'ro')
        plt.axis('equal')
        plt.title('Punto 2D')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.grid()
        plt.show()
    def tiempo_de_ejecucion(func):
        def envoltura(*args,**kwards):
            import time
            tiempo_inicio = time.time()
            resultado = func(*args,**kwards)
            tiempo_final = time.time()
            print(f"Tiempo de ejecucion: {tiempo_final - tiempo_inicio:.10f} segundos")
            return resultado
        return envoltura
    @tiempo_de_ejecucion
    def distancia(self, other):
        return f"La distancia entre {self} y {other} es {np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)}"