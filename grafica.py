import numpy as np
import matplotlib.pyplot as plt
from sympy import *
import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


x,y = symbols('x,y')
f,g = map(Function, 'fg')
x0 = 0 # initial amount


ed4= Eq(Derivative(f(x),x)*2*x-(f(x)),3*x**2)
index_set = f(x)
x = np.zeros(ed4)

x[0] = x0


plt.plot(ed4, x)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
