import sympy

# Defino incognitas
x = sympy.symbols('x')
y = sympy.Function('y')



# definiendo la ecuación
eq = 1.0/2 * (y(x)**2 - 1)

# Condición inicial
ics = {y(0): 2}

# Resolviendo la ecuación
edo_sol = sympy.dsolve(y(x).diff(x) - eq)
edo_sol