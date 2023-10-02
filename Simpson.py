import numpy as np

class SimpsonsRule:
    @staticmethod
    def calculate(func, a, b, num_points):
        dx = (b - a) / num_points
        x = np.linspace(a, b, num_points + 1)
        integral = (dx / 3.0) * sum(func(x[i]) + 4 * func((x[i] + x[i + 1]) / 2) + func(x[i + 1]) for i in range(0, num_points, 2))
        return integral
