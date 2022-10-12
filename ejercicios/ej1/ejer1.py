from sympy.interactive import printing
printing.init_printing(use_latex=True)
from sympy import *
import numpy as np
import sympy as sp
import math
from sympy import init_printing
#Para un mejor despliegue de la ED

x,y = symbols("x y")
f,g =map(Function,'fg')

#ED : y'=y*x*sin(x)
ed = Eq(Derivative(f(x),x),f(x)*x*sin(x))

solucion=dsolve(ed,f(x))
print("El resultado es:")
pprint(solucion)