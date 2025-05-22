import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 7]
y = [2, 4, 8, 16, 128]

def newton(x, y, val):
    n = len(x)
    y = y.copy()  # avoid modifying original y
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            y[i] = (y[i] - y[i - 1]) / (x[i] - x[i - j])
    result = y[-1]
    for i in range(n - 2, -1, -1):
        result = result * (val - x[i]) + y[i]
    return result

# Calculate f(5)
f5 = newton(x, y, 5)
print("f(5) =", f5)

# Plot interpolation curve
x_range = np.linspace(x[0], x[-1], 200)
y_range = [newton(x, y, xi) for xi in x_range]

plt.plot(x_range, y_range, label='Newton Interpolation')
plt.scatter(x, y, color='blue', label='Data Points')
plt.scatter(5, f5, color='red', label=f'f(5) = {f5:.2f}', zorder=5)
plt.legend()
plt.grid()
plt.title("Newton's Divided Difference Interpolation")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
