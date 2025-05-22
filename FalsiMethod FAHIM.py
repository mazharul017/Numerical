#  Solution of Algebric & Transcendental Equation
#  RegulaFalsiMethod or FalsePositionMethod

import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

def f(x):
    return x**4-4*x-9
def falsiMethod(x1,x2,error):
    iteration=0
    prev=0
    results=[]
    while True:
        m=((x1*f(x2))-(x2*f(x1)))/(f(x2)-f(x1))
        if abs(prev-m)<=error: break
        fm=f(m)
        results.append([iteration,x1,x2,m,fm,abs(prev-m)])
        plt.plot([x1,x2],[f(x1),f(x2)], 'r--o')
        if fm<=0: x1=m
        else: x2=m
        prev=m
        iteration+=1
    return results,m
    
    
x1,x2,error=1,3,0.000001
results,m=falsiMethod(x1,x2,error)
column=["iteration","x1","x2","m","fm","Error"]
print(tabulate(results, headers=column, tablefmt="grid"))


plt.axhline(0, color="black", linestyle='--')
plt.axvline(x1, color="blue", linestyle='--')
plt.axvline(x2, color="blue", linestyle='--')
plt.grid()
# plt.show()

xp=np.linspace(x1-1,x2+1,100)
yp=f(xp)
plt.plot(xp,yp,'r-',label="f(x) = x^3 - 4*x - 9") # plt.plot(xp,yp)
# plt.show()

plt.scatter([x1,x2],[f(x1),f(x2)],color="black",zorder=5)
plt.scatter([m],[f(m)],color="green",zorder=5)
plt.text(x1,f(x1),"f(x1)")
plt.text(x2,f(x2),"f(x2)")
# plt.show()

plt.title("Regula Falsi Graph")
plt.xlabel("x value")
plt.ylabel("y value")
plt.legend()
plt.show()