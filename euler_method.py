import numpy as np
from viscous_decay import Viscous

class Euler_method:
# Euler's method
    def calcuate_euler_method(v0, t_span, tau):
        v = np.zeros(len(t_span))  # Initialize an array for velocity values
        v[0] = v0  # Set the initial value
        dt = t_span[1] - t_span[0]  # Time step
        for i in range(1, len(t_span)):
            dvdt = Viscous(v[i - 1], t_span[i - 1], tau)
            v[i] = v[i - 1] + dvdt * dt
        return v
