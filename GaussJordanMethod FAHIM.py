import numpy as np
from tabulate import tabulate

def GaussJordan(Aug):
    n=len(Aug)
    for i in range(n):
        Aug[i]=Aug[i]/Aug[i,i]
        for j in range(n):
            if (i!=j):
                Aug[j]=Aug[j]-(Aug[j,i]*Aug[i])
    print(Aug)
    return Aug[:,n]    # Aug[:, n] selects the last column of the augmented matrix

A=np.array([[2.0,5,10],
            [1,7,9],
            [4,5,6]])
B=np.array([2,3,2])

Aug=np.column_stack((A,B))
x=GaussJordan(Aug)

for i in range(len(x)):
    print(f"x{i+1}={x[i]}")