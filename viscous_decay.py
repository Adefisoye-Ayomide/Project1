class Viscous:
# Define the ODE function: dv/dt = -v/tau
    def define_viscous_decay(v, t, tau):
        dvdt = -v / tau
        return dvdt