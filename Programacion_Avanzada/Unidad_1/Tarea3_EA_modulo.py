# 1. Crear un modulo.py
import time

class Punto2D:
  def __init__(self,a,b):
    self.a = a
    self.b = b

  def __add__(self,other):
    return (self.a + other.a), (self.b + other.b)

  def __sub__(self,other):
    return (self.a - other.a), (self.b - other.b)

  def __rmul__(self, scalar1):
        # CORRECION PARA OBTENER 4*A+B
    return Punto2D(scalar1*self.a, scalar1*self.b)

  def __call__(self,escalar1):
    return Punto2D(self.a * escalar1, self.b * escalar1)

  def __str__(self):
    return f'({self.a}, {self.b})'
  
  def tiempo_de_ejecucion(func):
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución de {func.__name__}: {fin - inicio} segundos")
        return resultado
    return envoltura

  @tiempo_de_ejecucion
  def distancia1(self,other):
    return f"La distancia es de {round((((self.a - other.a)**2) + ((self.b - other.b)**2))**0.5,1)} unidades"
    # + DECORADOR

  def modulo(self):
    return (((self.a)**2) + ((self.b)**2))**0.5

  def __abs__(self):
    return self.modulo()

  def grafica(self):
    import matplotlib.pyplot as plt
    plt.plot(self.a,self.b,marker ="o",label= f'({self.a}, {self.b})')   
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.title(f'Punto({self.a}, {self.b})')
    plt.grid()
    plt.legend(loc=4)
    plt.show()




