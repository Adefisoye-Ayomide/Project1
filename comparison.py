import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the ODE function: dv/dt = -v/tau
def viscous_decay(v, t, tau):
    dvdt = -v / tau
    return dvdt

# Parameters
tau = 1.0  # Characteristic time constant
v0 = 2.0   # Initial velocity
t_span = np.linspace(0, 10, 100)  # Time span for integration

# Solve the ODE using odeint
v_solution = odeint(viscous_decay, v0, t_span, args=(tau,))

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t_span, v_solution, label="ODE Solution (odeint)")
plt.xlabel("Time (t)")
plt.ylabel("Velocity (v)")
plt.legend()
plt.title("Decay of Momentum in a Viscous Fluid (ODE Solution)")
plt.grid(True)
plt.show()
