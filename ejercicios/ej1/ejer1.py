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

        #Ecuacion 1
        print("Ecuacion 1:")
        ed= Eq(Derivative(f(x),x),(f(x)(x*2)-f(x))/(f(x)+1))
        ci = {f(3): -1}

        solucion= dsolve(ed,f(x), ics=ci)
        print("El resultado es: ")
        pprint(solucion)
        