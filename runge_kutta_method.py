import numpy as np

class Runge_kutta:
    @staticmethod
    def viscous_decay(v, t, tau):
        dvdt = -v / tau
        return dvdt
    
# 4th order Runge-Kutta method
    def calculate_runge_kutta_method(self, v0, t_span, tau):
        v = np.zeros(len(t_span))  # Initialize an array for velocity values
        v[0] = v0  # Set the initial value
        dt = t_span[1] - t_span[0]  # Time step
        for i in range(1, len(t_span)):
            t = t_span[i - 1]
            k1 = dt * Runge_kutta.viscous_decay(v[i - 1], t, tau)
            k2 = dt * Runge_kutta.viscous_decay(v[i - 1] + k1 / 2, t + dt / 2, tau)
            k3 = dt * Runge_kutta.viscous_decay(v[i - 1] + k2 / 2, t + dt / 2, tau)
            k4 = dt * Runge_kutta.viscous_decay(v[i - 1] + k3, t + dt, tau)
            v[i] = v[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        return v
