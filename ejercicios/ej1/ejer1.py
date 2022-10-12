from sympy.interactive import printing
printing.init_printing(use_latex=True)
from sympy import *
import numpy as np
import sympy as sp
import math
from sympy import init_printing

class Primero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        x,y = symbols("x y")

    def ecuacion1(self, x, y):
        #ED : y'=(x**2*y-y)/(y+1)
        ed = Eq(Derivative(y,x),((y*(x**2)-y)/(y+1))
        
        sol = dsolve(ed,y)
        print("El resultado es:")
        pprint(sol)