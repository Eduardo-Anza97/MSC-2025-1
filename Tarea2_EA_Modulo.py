
#1. Crear un mo dulo funciones.py:

"""
Este modulo contiene funciones designadas en la tarea 2
de Programación Avanzada de alumno Eduardo Anza
"""

######## función 1 ########
def f(*x):
  """ Ingresa valores de x para la función x^2.
  """
  print("Los valores de x ingresados para la función x^2 son:")
  return[x**2 for x in x]

######## función 2 ########
import math
def g(*x_y):
  """ Ingresa valores de (x,y) para la función sen(x)*cos(y).
  """
  print("Los valores de (x,y) ingresados para la función sen(x)*cos(y) son:")
  return[(math.sin(x)*math.cos(y)) for (x,y) in x_y]

######## función 3 ########
def h(*x_y_z):
  """ Ingresa valores de (x,y,z) para la función x*y*z.
  """
  print("Los valores de (x,y,z) ingresados para la función sen(x)*cos(y) son:")
  return[(x*y*z) for (x,y,z) in x_y_z]

###########################

#2. Crear una clase Funcion:

#inicio class
class Funcion:
  """
  S
  """
  def __init__(self,*inputs):
    self.inputs = inputs
  #
  def f1(self,*inputs):
    return[x**2 +(y+z)*0 for (x,y,z) in inputs] #ajuste de y,z para no provocar error si el usuario ingresa una terna
  #
  import math
  def g1(self,*inputs):
    return[(math.sin(x)*math.cos(y)+z*0) for (x,y,z) in inputs] #ajuste de z para no provocar error si el usuario ingresa una terna
  #
  def h1(self,*inputs):
    return[(x*y*z) for (x,y,z) in inputs]

evaluar = Funcion()
















