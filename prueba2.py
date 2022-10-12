
from sympy import *
import sympy
import math
from sympy.interactive import printing
from IPython.display import display
import scipy as sp
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
import numpy as np


x,y = symbols('x,y')
f,g = map(Function, 'fg')

#Ecuacion 1
print("Ecuacion 1:")

ed1 = Eq(Derivative(f(x),x),(f(x)(x*2)-f(x))/(f(x)+1))
pprint(ed1)
ci = {f(3): -1}

solucion1= dsolve(ed1,f(x), ics=ci)
print("El resultado es: ")
pprint(solucion1)