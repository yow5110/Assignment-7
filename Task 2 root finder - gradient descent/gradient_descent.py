# Week 9 Task 2 
# Write a function to find the minimum of a function by moving in the downhill direction (gradient descent).
# Use the function to find the equilibrium distance of a LJ system with two atoms. 
# NOTE: Pay attention that the LJ force already has the opposite sign wrt the derivative of the potential.
# Compare the accuracy of the result with the analytic result and with the bisection method and study the dependence of the 
# accuracy on the timestep.


import numpy as np
epsilon = 4.e-4 # in a.u.
sigma = 6 # in a.u.
r_min_analytical = 6*(2**(1/6))
t = 1

def flj(distance):
  """ 
  Function to compute the magnitude of the force acting on a pair of particles
  interacting through the Lennard-Jones potential
  Input variables
    distance: distance betwewen the particles
  """
  flj = (-1)*24*epsilon*(sigma**6/distance**7 - 2*(sigma**12/distance**13))
  return flj

def gradient_descent(df, x, tol = 1.e-10): 
  """
  Function to reach a local minimum of a function by following the direction opposite to its first derivative
  Input variables
    df: derivative of the function of which we search the minimum
    x: initial guess for the minimum of the function
    tol: accuracy of the result
  Output results
    xmin: value of the argument of the function for which the function has a local (or global) minimum
  """
  xmin = x # TASK 1: Armand Parada Jackson
  
  while(np.abs(df(xmin)) > tol):
      xmin = xmin + t*df(xmin)
  return xmin

def bisection(a,b,f,dx=1.e-10):
  """
  Function to compute the zero of a function using the bisection method
  Input variables
    a,b : extremes of the interval. 
    f: function of which we search the zero
    dx: optional, final size of the interval containing the zero (i.e. error in the estimate of the zero)
  NOTE: f(a) should have opposite sign wrt f(b) and f should be continuous in [a,b]
  """
  if (f(a)*f(b) > 0.0):  
      print("")
      print(f(a))
      print(f(b))
      print("")
      print("Error: the function f(x) should assume values of opposite sign in a and b")
      print("")
  else:
    sign = ( 1 if f(a)>f(b) else -1 )
    while b-a > dx :
      tmp=(a+b)/2
      if ( sign*f(tmp) > 0):
        a=tmp
      else:
        b=tmp
  return (a+b)/2

# Test the gradient_descent() function on the Lennard-Jones system, i.e. pass the LJ force to it. 
# TASK 2: compare the results with the bisection method a the analytic expression for the position of the minimum
print("")
initGuess = float(input("Enter guess for equilibrium distance: "))
print("")
  
estimate = gradient_descent(flj, initGuess)
error = r_min_analytical - estimate

bisectionEstimate = bisection(1, 10, flj)
bisectionError = r_min_analytical - bisectionEstimate
  
print("Equilibrium Distance Estimate: {:.8f}".format(estimate))
print("")
print("Error: {:.8f}".format(error))
print("")
print("")
print("Estimate using Bisection: {:.8f}".format(bisectionEstimate))
print("")
print("Bisection Error: {:.8f}".format(bisectionError))
