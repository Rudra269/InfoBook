import numpy as np
import matplotlib.pyplot as plt


A = np.array([[1, 2], [3, 4]])
print(A)

print()

B = np.array([[1], [2]])
print(B)

print()
R = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)], [np.sin(np.pi/4), np.cos(np.pi/4)]])
print(R)

print()

print(np.dot(A, B))

print()

print(A+A)

print()

print(np.transpose(np.dot(A, B)))

print()

print(np.dot(np.transpose(B), A))

print()

print(np.dot(R, R))

print()

x = np.linspace(-1.5, 3, 100)
y = np.exp(x)
plt.plot(x, y)
plt.show()

p1 = np.array([[0, 0, 5], 
               [18, 5, -5]])

np = p1.shape[1]

print(np)