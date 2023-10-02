import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from Riemann import RiemannSum
from Trapezoid import TrapezoidalRule
from Simpson import SimpsonsRule

# Define the density function ρ(x)
def density_function(x):
    return x 

def input_density_function():
    while True:
        try:
            expression = input("Enter a linear function for ρ(x) (e.g., '2*x + 3'): ")
            rho_function = lambda x: eval(expression)
            if callable(rho_function):
                return rho_function
            else:
                print("Invalid input. Please enter a valid linear function.")
        except Exception as e:
            print(f"Invalid input. Please enter a valid linear function. Error: {e}")

#Function to validate and parse the integration limits input
def input_integration_limits():
    while True:
        try:
            a = float(input("Enter lower limit of integration (a): "))
            b = float(input("Enter upper limit of integration (b): "))
            if a < b:
                return a, b
            else:
                print("Invalid input. Lower limit should be less than upper limit.")
        except ValueError:
            print("Invalid input. Please enter numerical values.")

a = 0
b = 2

# Ask the user if they want to input custom values or use defaults
user_choice = input("Do you want to enter custom parameters? (yes/no): ").strip().lower()
if user_choice == "yes":
    density_function = input_density_function()
    a, b = input_integration_limits()

# Calculate the definite integral using different methods
num_points = 1000

# Using Riemann Sum
riemann_sum_calculator = RiemannSum()
integral_riemann = riemann_sum_calculator.calculate(density_function, a, b, num_points)

# Using Trapezoidal Rule
trapezoidal_rule_calculator = TrapezoidalRule()
integral_trapezoidal = trapezoidal_rule_calculator.calculate(density_function, a, b, num_points)

# Using Simpson's Rule
simpsons_rule_calculator = SimpsonsRule()
integral_simpsons = simpsons_rule_calculator.calculate(density_function, a, b, num_points)

integral_scipy, _ = quad(density_function, a, b)

# Compare with the analytic solution (if available)
analytic_result = (b**2 - a**2) / 2.0  # Analytic solution for x^2

# Print the results
print(f"Riemann Sum: {integral_riemann}")
print(f"Trapezoidal Rule: {integral_trapezoidal}")
print(f"Simpson's Rule: {integral_simpsons}")
print(f"Scipy Integration: {integral_scipy}")
# print(f"Analytic Solution: {analytic_result}")

# Plot the density function
x_values = np.linspace(a, b, 1000)
y_values = [density_function(x) for x in x_values]

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="Density Function")
plt.fill_between(x_values, 0, y_values, where=[a <= x <= b for x in x_values], alpha=0.2, label="Integral Area")
plt.xlabel("x")
plt.ylabel("Density ρ(x)")
plt.legend()
plt.title("Definite Integral of Density Function")
plt.grid(True)
plt.show()

