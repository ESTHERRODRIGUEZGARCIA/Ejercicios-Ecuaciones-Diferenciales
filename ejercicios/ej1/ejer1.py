# importando modulos necesarios
%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np
import sympy 
from scipy import integrate

# imprimir con notación matemática.
sympy.init_printing(use_latex='mathjax')

# Resolviendo ecuación diferencial
# defino las incognitas
x = sympy.Symbol('x')
y = sympy.Function('y')

# expreso la ecuacion
f = 6*x**2 - 3*x**2*(y(x))
sympy.Eq(y(x).diff(x), f)