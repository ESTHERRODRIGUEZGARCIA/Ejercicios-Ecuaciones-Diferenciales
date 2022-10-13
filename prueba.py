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