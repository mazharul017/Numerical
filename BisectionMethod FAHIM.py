#  Solution of Algebric & Transcendental Equation
#  BisectionMethod or BolzanoMethod 

import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

def f(x):
    return x**3-4*x-9
def bisectionMethod(x1,x2,error):
    iteration=0
    prev=0
    results=[]
    while True:
        m=(x1+x2)/2
        if abs(prev-m)<=error:
            break
        fm=f(m)
        results.append([iteration,x1,x2,m,fm,abs(prev-m)])
        plt.plot([x1,x2],[f(x1),f(x2)],'r--o')
        if fm<=0:
            x1=m
        else:
            x2=m
        iteration+=1
        prev=m
    return results,m
        

x1,x2,error=2,3,0.001 # f(2)=negative, f(3)=positive
results,m=bisectionMethod(x1,x2,error)
column=["Iteration","x1(-)","x2(+)","m", "f(m)","Error"]
print(tabulate(results, headers=column, tablefmt="grid"))
# plt.show()

plt.axhline(0, color="black", linestyle='--')
plt.axvline(x1, color="blue", linestyle='--')
plt.axvline(x2, color="blue", linestyle='--')
plt.grid()

xp=np.linspace(x1-1, x2+1, 100)
yp=f(xp)
plt.plot(xp,yp,'r-', label="f(x)=x^3-4x-9")

plt.scatter([x1,x2],[f(x1),f(x2)],color="black",zorder=5)
plt.scatter([m],[f(m)],color="green",zorder=5)
plt.text(x1,f(x1),"f(x1)")
plt.text(x2,f(x2),"f(x2)")

plt.title("Bisection Graph")
plt.xlabel("X Value")
plt.ylabel("Y Value")
plt.legend()
plt.show()