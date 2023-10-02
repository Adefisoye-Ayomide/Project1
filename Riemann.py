class RiemannSum:
    @staticmethod
    def calculate(func, a, b, num_points):
        dx = (b - a) / num_points
        integral = sum(func(a + i * dx) * dx for i in range(num_points))
        return integral
