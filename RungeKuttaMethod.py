# RungeKuttaMethodOfFourthOrder

import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

def f(x,y):
    return x+y
x0,y0=0,1
x,y=x0,y0
h=0.5
n=4
xres,yres=[],[]

for i in range(n):
    k1=h*f(x,y)
    k2=h*f(x+h/2,y+k1/2)
    k3=h*f(x+h/2,y+k2/2)
    k4=h*f(x+h,y+k3)

    y=y+(k1+2*k2+2*k3+k4)/6
    x=x+h

    xres.append(x)
    yres.append(y)


plt.plot(xres, yres, 'r-o')
plt.title("Runge-Kutta Method (RK4)")
plt.grid()
plt.show()