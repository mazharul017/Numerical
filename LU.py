import numpy as np

def back_sub(U, y):
    n = len(U)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x

def forward_sub(L, b):
    n = len(L)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])  # L[i,i] = 1, no division needed
    return y

def LU(A, B):
    n=len(A)
    L=np.eye(n)
    U=A.copy().astype(float)

    for i in range(n):
        for j in range(i+1,n):
            factor=U[j,i]/U[i,i]
            L[j,i]=factor
            U[j]-=factor*U[i]

    y = forward_sub(L, B)
    x = back_sub(U, y)
    return L, U, x

A = np.array([[2, 5, 10],
              [1, 7, 9],
              [4, 5, 6]])
B = np.array([2, 3, 2])

L,U,x=LU(A, B)

# Output
print("L =\n", L, "\n")
print("U =\n", U, "\n")
print("L and U=\n", np.dot(L, U), "\n")

# Solution
for i in range(len(x)):
    print(f"x{i+1} = {x[i]:.4f}")