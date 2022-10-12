import sympy

# Defino incognitas
x = sympy.symbols('x')
y = sympy.Function('y')

# Defino la función
ec = y(x)**2 + x**2 -1


sympy.solve(ec)