import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import numpy as np
import matplotlib.pyplot as plt


x,y = symbols('x,y')
f,g = map(Function, 'fg')
x0 = 0 # initial amount


ed4= Eq(Derivative(f(x),x)*2*x-(f(x)),3*x**2)
index_set = f(x)


plt.plot(ed4, f(x))
plt.xlabel('x')
plt.ylabel('y')
plt.show()
