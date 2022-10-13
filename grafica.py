



import matplotlib.pyplot as plt
from numpy import *
from scipy.integrate import odeint
def df(y,x):
    y1, y2= y[0], y[1] #Se le asigna una posición en el vector solución a y1 y y2
    dy1=y2
    dy2=-x*y2-20*sin(y1)
    return [dy1,dy2]
y0 =[0,1] # Condiciones iniciales
x = linspace(0,6,500) # Definición del rango
sol = odeint(df, y0, x) # la función odeint se encarga de dar los argumentos a la función df(el rango “x” y la variable “y”)
y=sol[:,0] #toma el vector correspondiente a la solución de y1
plt.plot(x,y)
plt.grid(True)
plt.show()