# Week 9 Task 1
# Write your own version of the sqrt() function using Newton's algorithm to find the zero of a function
# In particular, express x=sqrt(alpha) as the zero of the function f(x)=x**2-alpha

import numpy as np

def newton(f, df, x, tol=1.e-10): 
  """
  Function to compute the zero of a function using Newton's method
  Input variables
    f: function of which we search the zero
    df: derivative of function f
    x: initial guess for the zero of the function
    tol: accuracy of the result
  """
  dx = 1.
  while abs(dx) > tol:
    dx = - f(x)/df(x) 
    x += dx
  return x
