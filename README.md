#Computational Physics Project1 Repository.

Welcome to my computational physics project1. The goal of the project is to numerically solve a 1D ODE and a simple integral using methods like euler approximations, runge-kutta, trapezoid rule, etc., make sense of the physics behind it, and then compare the result with the result obtained from using a standard library like scipy.
To run this program, there are certain prereuqisites that must be met on your machine. Ensure you have the following installed: 
- Python 3
- Numpy
- SciPy (for the integration code comparison)
- Matplotlib (for visualization)
## Running the ODE code
First step is to clone the Github repository to your local machine:
Navigate to the directory containing the repository
Run the file named "main_ode.py"
There are options to either run the code with default values or from user input. If the user selects the option that allows user to give input, then the user must provide input constant for the ODE probem accordingly. such constants include velocity, relaxation time, time-step, counts, etc.
Note that: the main_ode.py is the main code to be run that give the required output. other codes that defined functions that calculated the ODE are imported into the main_ode.py code. Examples of that are the files named: euler_method.py, runge_kutta_method.py, comparison.py, etc which are all in the same folder.

## Running the Integration code
This is quite similar to the steps required to run the ODE code. In this case though, there will not be a need to clone repository as everything is already cloned from the first step.
Simply run the file named "main_Integration.py". This constains the main action where other functions/packages are imported. Examples of those are the: Riemann.py which contains the function that solves the integration using the Riemann method, Simpson.py, and Trapezoid.py.
When each of the main.py code is run, there will be output that gives the actual result of the problem (ODE or Integral), as well as a plot that visualizes the result for the user.

## You have  successfully run the ODE problem and the definite integral problem codes from this repository.

Thank you!!

Best,
Matthew
