# Interpolation with unequal interval
# lagrange's Interpolation Formula

import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

def lagrange(x,y,x1):
    sum=0
    for i in range(len(x)):
        val1=1
        val2=1
        for j in range(len(x)):
            if (i!=j):
                val1*=(x1-x[j])
                val2*=(x[i]-x[j])
        sum+=(val1/val2)*y[i]
    return sum


x=[1,2,3,4,7] # x
y=[2,4,8,16,128] #f(x)
x1=5 # question 
results=lagrange(x,y,x1)
print("f(5)=", results)

x11=np.linspace(x[0],x[-1],100)
y11=lagrange(x,y,x11)
plt.plot(x11,y11)

plt.scatter(x1,results,color="red",zorder=5)
plt.show()
