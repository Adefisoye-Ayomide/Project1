class TrapezoidalRule:
    @staticmethod
    def calculate(func, a, b, num_points):
        dx = (b - a) / num_points
        integral = 0.5 * dx * (func(a) + func(b) + 2 * sum(func(a + i * dx) for i in range(1, num_points)))
        return integral
