import sympy
sympy.init_printing(use_latex='mathjax')
# Defino incognitas
x = sympy.symbols('x')
y = sympy.Function('y')



# definiendo la ecuación

sympy_Eq(y(x).diFf(x)+(2*x"y(x)*-2+1)/(2°x**2*y(x)))

# Condición inicial
ics = {y(0): 2}

# Resolviendo la ecuación
sympy.dsolve(y(x).diff(x)+(2°x*y(x)*-2+1)/(2*x*-2-y(x)))
