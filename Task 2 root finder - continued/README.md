# Week 9 Task 2
We can actually relieve the user of providing the derivative of f() in the Newton-Raphson method. Write another Newton-Raphson method newton2() that numerically calculates df (within  newton2()). Test your newton2() on the sine function again to find a root at pi, this time only providing the sine fucntion itself but not its derivative.

With this new-found freedom, test your newton2() on our in-class projectile exercise: given that the projectile starts out at a speed of 30 m/s, an angle of 30 degrees above ground level, how far can it reach? g = 9.8 m/s^2 and air drag linear coefficient b = 1 s^-1. We already found out in class that the answer is near 23.29m. You may find that you can only get this solution if your initial guess is roughly between 21 and 25 m; otherwise the code crashes. Explain why. 

Hint: Plot out the f(R) function against R and discuss how the algorithm will fail if you start from R>25 and R<21.

(The intention of this problem is to show that the function could be ill-behaved around your desired solution such that you need to start really close to make the Newton-Raphson method work.)