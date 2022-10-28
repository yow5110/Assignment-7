# Week 9 Task 2

import numpy as np

def newton2(f, x, tol=1.e-5): 
   # calculate f(x)
   # calculate df(x) by taking finite differences numerically
   # perform Newton-Raphson method
   return x
 
#demonstrate how you can find a root at pi using your newton2()
x_init = 
result = newton2(np.sin, x_init)
print(result)


def f(R):
    g = 9.8 # m/s^2 
    b = 1 # /s
    angle = 30 # degrees
    v0x = 30 * np.cos(angle/180*np.pi)
    v0z = 30 * np.sin(angle/180*np.pi)
    res = R/v0x * (v0z + g/b) + g/b**2 * np.log(1-b*R/v0x)
    return res


# An initial guess of 24 works. But the algorithm is quite fragile and breaks for initial guess smaller than 21 or larger than 25.

R_init = 24
result = newton2(f, R_init)
print(result)

#plot out f() to finish the discussions on why the root search fails if R_init<21 or >25
import matplotlib.pyplot as plt


