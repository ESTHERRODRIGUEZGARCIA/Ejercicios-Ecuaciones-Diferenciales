# este me devuelve la gráfica
from sympy import *
import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


x,y = symbols('x,y')
f,g = map(Function, 'fg')


# function that returns dy/dt

ed4= Eq(Derivative(f(x),x)*2*x-(f(x)),3*x**2)
pprint(ed4)



# plot results
plt.plot(x,f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()


print("Ecuacion 4:")
ed4= Eq(Derivative(f(x),x)*2*x-(f(x)),3*x**2)
pprint(ed4)

solucion4= dsolve(ed4,f(x))
print("El resultado es: ")
pprint(solucion4)







####################


import matplotlib.pyplot as plt
from numpy import *
from scipy.integrate import odeint
def df(y,x):
    y1, y2= y[0], y[1] #Se le asigna una posición en el vector solución a y1 y y2
    dy1=y2
    dy2=-x*y2-20*sin(y1)
    return [dy1,dy2]
y0 =[0,1] # Condiciones iniciales
x = linspace(0,6,500) # Definición del rango
sol = odeint(df, y0, x) # la función odeint se encarga de dar los argumentos a la función df(el rango “x” y la variable “y”)
y=sol[:,0] #toma el vector correspondiente a la solución de y1
plt.plot(x,y)
plt.grid(True)
plt.show()