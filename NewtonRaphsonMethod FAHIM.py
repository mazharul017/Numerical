#  Solution of Algebric & Transcendental Equation
#  NewtonRaphsonMethod

import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

def f1(x):
    return x**3-3*x-5
def f2(x): # f2(x)=f1'(x)
    return 3*x**2-3
def newtonRaphsonMethod(x1,error):
    iteration=1
    results=[]
    prev=0
    while True:
        m=x1-(f1(x1)/f2(x1))
        results.append([iteration, x1, m])
        plt.scatter([x1], [f1(x1)], color="black", zorder=5)
        if abs(prev-m)<=error:
            break
        x1=m
        prev=m
        iteration+=1
    return results,m

x1,error=2,0.00001 # f(2)=-3(near by 0 and negative)
results,m=newtonRaphsonMethod(x1, error)
columns=["Iteration","Xn","Xn+1"]
print(tabulate(results, headers=columns, tablefmt="grid"))
# plt.show()

plt.axhline(0,color="black",linestyle="--")
plt.axvline(x1,color="blue",linestyle="--")
plt.grid()

xp=np.linspace(x1-5, x1+5, 100)
yp=f1(xp)
plt.plot(xp,yp,"r-",label="f(x)=x^3-3x-5")

plt.scatter([x1],[f1(x1)],color="red",zorder=5)
plt.scatter([m],[f1(m)],color="green",zorder=5)
plt.text(x1,f1(x1),"f(x)")

plt.title("Newton Raphson Graph")
plt.xlabel("X value")
plt.ylabel("Y value")
plt.legend()
plt.show()