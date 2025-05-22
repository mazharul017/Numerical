# EulerModifiedMethod or RungeKuttaMethodOf2ndOrder

import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

def f(x,y):
    return x+y
x0,y0=0,1
x,y=x0,y0
h=0.5
n=4
xres,yres=[],[]
for i in range(n):
    y=y+h*f(x,y)
    x=x+h
    xres.append(x)
    yres.append(y)

plt.plot(xres,yres,'r-o')
plt.title("Euler Method")
plt.grid()
plt.show()