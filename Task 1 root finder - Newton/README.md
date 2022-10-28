# Week 9 Task 1
In addition to the bisection method, Newton's method is another algorithm to find zeros of function. It works as follows:

1. We start from an initial guess of the value of the zero, <a href="https://www.codecogs.com/eqnedit.php?latex=x_0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_0" title="x_0" /></a>. 
2. We assume that the function is linear, with slope given by the value of its first derivative at the point considered. With this assumption, we can calculate the zero of the function from basic geometry: <a href="https://www.codecogs.com/eqnedit.php?latex=x_{n&plus;1}=x_{n}-\frac{f(x_n)}{f'(x_n)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{n&plus;1}=x_{n}-\frac{f(x_n)}{f'(x_n)}" title="x_{n+1}=x_{n}-\frac{f(x_n)}{f'(x_n)}" /></a>.
3. We iterate this process until the change in our estimate is smaller than a certain threshold. 

The algorithm requires to provide both the function and its first derivative. This method can be used to evaluate a function of which we know the inverse, e.g. it allows to compute <a href="https://www.codecogs.com/eqnedit.php?latex=\sqrt&space;x" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sqrt&space;x" title="\sqrt x" /></a>, given that we know how to compute <a href="https://www.codecogs.com/eqnedit.php?latex=x^2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x^2" title="x^2" /></a>. In fact, it is easy to see that we can find <a href="https://www.codecogs.com/eqnedit.php?latex=x=\sqrt&space;a" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x=\sqrt&space;a" title="x=\sqrt a" /></a> by looking for the zero of the function <a href="https://www.codecogs.com/eqnedit.php?latex=f(x)=x^2-a" target="_blank"><img src="https://latex.codecogs.com/gif.latex?f(x)=x^2-a" title="f(x)=x^2-a" /></a>.

TASK: The file newton_sqrt.py contains a user defined newton() function that implement the above method. Use the newton() function to implement your numerical version of the square root function. 

EXPECTED OUTCOME: Compute the square root of a few numbers using your function and compare the results with the numpy.sqrt() ones.
