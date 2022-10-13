#importando funciones 
from sympy import *
import math


x,y = symbols('x,y')
f,g = map(Function, 'fg')

# ecuación 1
print("Ecuacion 1:")
ed1= Eq(Derivative(f(x),x),((f(x)*x**2-f(x))/(f(x)+1)))
pprint(ed1)
ci = {f(3): -1}

solucion1= dsolve(ed1,f(x), ics=ci)
print("El resultado es: ")
pprint(solucion1)

#Ecuacion 2
print("Ecuacion 2:")
ed2= Eq(Derivative(f(x),x)*sin(x),f(x)*log(f(x)))
pprint(ed2)
ci = {f(math.pi/2): math.e}

solucion2= dsolve(ed2,f(x), ics=ci)
print("El resultado es: ")
pprint(solucion2)

#Ecuacion 3
print("Ecuacion 3:")
ed3= Eq(Derivative(f(x),x)-(f(x)/(x-2)),2*(x-2)**2)
pprint(ed3)

solucion3= dsolve(ed3,f(x))
print("El resultado es: ")
pprint(solucion3)

#Ecuacion 4
print("Ecuacion 4:")
ed4= Eq(Derivative(f(x),x)*2*x-(f(x)),3*x**2)
pprint(ed4)

solucion4= dsolve(ed4,f(x))
print("El resultado es: ")
pprint(solucion4)

#Ecuacion 5 que es la que nos quería poner en realidad javi profe
print("Ecuacion 5:")
ed5= Eq(Derivative(f(x),x)*2*x-x,3*x**2)
pprint(ed5)

solucion5= dsolve(ed5,f(x))
print("El resultado es: ")
pprint(solucion5)

