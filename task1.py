import matplotlib.pyplot as plt
import numpy as np

def hermite_curve(p1, p2, v1, v2):
    t = np.linspace(0, 1, 100)
    h1 = 2*t**3 - 3*t**2 + 1
    h2 = -2*t**3 + 3*t**2
    h3 = t**3 - 2*t**2 + t
    h4 = t**3 - t**2

    x = h1*p1[0] + h2*p2[0] + h3*v1[0] + h4*v2[0]
    y = h1*p1[1] + h2*p2[1] + h3*v1[1] + h4*v2[1]

    plt.plot(x, y, 'b')
    plt.scatter([p1[0], p2[0]], [p1[1], p2[1]], color='red')
    plt.title("Крива Ерміта")
    plt.axis('equal')
    plt.grid()
    plt.show()

hermite_curve((0, 0), (4, 4), (5, 0), (0, -5))
