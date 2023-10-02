import numpy as np
import matplotlib.pyplot as plt
from euler_method import Euler_method
from runge_kutta_method import Runge_kutta
from viscous_decay import Viscous

# # Define the ODE function: dv/dt = -v/tau
# def viscous_decay(v, t, tau):
#     dvdt = -v / tau
#     return dvdt

# Function to solve and plot the ODE with user input
def solve_and_plot_with_user_input():
    v0 = float(input("Enter initial velocity (m/s): "))
    tau = float(input("Enter time constant (s): "))
    t_start = float(input("Enter start time (s): "))
    t_end = float(input("Enter end time (s): "))
    num_points = int(input("Enter the number of time points: "))

    t_span = np.linspace(t_start, t_end, num_points)

    try:
        v_euler = Euler_method(v0, t_span, tau)
        v_rk = Runge_kutta(v0, t_span, tau)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(t_span, v_euler, label="Euler's Method")
    plt.plot(t_span, v_rk, label="4th Order Runge-Kutta")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.legend()
    plt.title("Decay of Momentum in a Viscous Fluid")
    plt.grid(True)
    plt.show()

# Function to solve and plot the ODE with default values
def solve_and_plot_with_default_values():
    v0 = 2.0
    tau = 1.0
    t_start = 0.0   
    t_end = 10.0
    num_points = 100

    t_span = np.linspace(t_start, t_end, num_points)

    try:
        v_euler = Euler_method(v0, t_span, tau)
        v_rk = Runge_kutta(v0, t_span, tau)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(t_span, v_euler, label="Euler's Method")
    plt.plot(t_span, v_rk, label="4th Order Runge-Kutta")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.legend()
    plt.title("Decay of Momentum in a Viscous Fluid")
    plt.grid(True)
    plt.show()

# Main function to choose between user input and default values
def main():
    choice = input("Do you want to enter custom parameters? (yes/no): ").strip().lower()
    if choice == "yes":
        solve_and_plot_with_user_input()
    elif choice == "no":
        solve_and_plot_with_default_values()
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
