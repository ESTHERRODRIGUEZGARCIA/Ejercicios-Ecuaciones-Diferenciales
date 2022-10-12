# importo librerías
from sympy import *
import numpy as np
import sympy 
from sympy.interactive import printing
printing.init_printing(use_latex=True)
import math
from sympy import init_printing
import matplotlib.pyplot as plt

x,y = symbols('x,y')
f,g = map(Function,'fg')

#Ecuacion 1
print("Ecuacion 1:")
ed= Eq(Derivative(f(x),x),(f(x)(x*2)-f(x))/(f(x)+1))
ci = {f(3): -1}

solucion= dsolve(ed,f(x), ics=ci)
print("El resultado es: ")
pprint(solucion)