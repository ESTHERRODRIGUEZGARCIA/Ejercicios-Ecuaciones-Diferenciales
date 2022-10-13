#importando funciones 
from sympy import *
import sympy
import math
import numpy as np
import matplotlib.pyplot as plt

class Primero:
    def __init__(self, x, y):
        self.x = x
        self.f = f
        x = symbols("x")
        f =map(Function,'f')

    def ecuacion1(self, x, y):

        #ED : y'=(x**2*y-y)/(y+1)

        #Ecuacion 1
        print("Ecuacion 1:")
        ed= Eq(Derivative(y,x),(y(x*2)-y)/(y+1))
        ci = {y(3): -1}

        solucion= dsolve(ed,y, ics=ci)
        print("El resultado es: ")
        pprint(solucion)