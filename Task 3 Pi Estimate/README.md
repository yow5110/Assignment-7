# Week 9 Task 3

In this assignment we will estimate the value of pi using random numbers. Imagine throwing darts randomly at a circle with radius 1 centered at the origin. 

If we throw enough darts at it, count the number of darts n_in that landed inside the circle , and count the number of darts n_total that landed inside the square that circumscribes the circle (running from -1 to 1 in x and in y), then we can estimate pi by 4*n_in/n_total. 

Write a loop, where in each step we generate two random real numbers between -1 and 1 to represent the x and y coordinate of a dart, and keep track of the number of darts that fall within the unit circle. At the end of the loop, print the estimate of pi.

EXPECTED OUTCOME: In the limit of large n you should approach pi. 
