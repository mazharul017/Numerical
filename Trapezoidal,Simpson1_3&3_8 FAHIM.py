# implementations of Trapezoidal Rule, Simpson's 1/3 Rule, and Simpson's 3/8 Rule for numerical integration
# trapezoidal,Simpson1_3 and Simpson3_8 Rule

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from tabulate import tabulate

def f(x):
    return x**2    # You can replace this with any function
def trapezoidal(a,b,n):
    h=(b-a)/n
    result=f(a)+f(b)
    for i in range(1,n):
        result+=2*f(a+i*h)
        
    return (h/2)*result

def Simpson1_3(a,b,n):  
    h=(b-a)/n
    result=f(a)+f(b)
    for i in range(1,n):
        if i%2==0: 
            result+=2*f(a+i*h)
        else: 
            result+=4*f(a+i*h)

    return (h/3)*result

def Simpson3_8(a,b,n):
    h=(b-a)/n
    result=f(a)+f(b)
    for i in range(1,n):
        if(i%3==0):
            result+=2*f(a+i*h)
        else:
            result+=3*f(a+i*h)
            
    return (3*h/8)*result

# Example usage
a=0
b=1
n=6  # Choose n appropriately: even for 1/3, multiple of 3 for 3/8

print("Trapezoidal: ", trapezoidal(a, b, n))
print("Simpson 1/3 :", Simpson1_3(a, b, n))
print("Simpson 3/8 :", Simpson3_8(a, b, n))