import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

y, x = np.ogrid[-10:10:1000j, -10:10:1000j]
plt.contour(
    x.ravel(), y.ravel(), y-0*x, [0])#x-axis
plt.contour(
    x.ravel(), y.ravel(), x-0*y, [0])#y-axis
plt.contour(
    x.ravel(), y.ravel(), y-(x**3-2*x)/(2*(x**2-5)), [0])#actual expression

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('y-(x**3-2*x)/(2*(x**2-5))')

plt.show()









