# Week 9 Task 1
In addition to the bisection method, The Newton-Raphson method is another algorithm to find zeros of function. It works as follows:

<a title="Original:  Olegalexandrov Vector:  Pbroks13, Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Newton_iteration.svg"><img width="512" alt="Newton iteration" src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Newton_iteration.svg/512px-Newton_iteration.svg.png"></a>

1. We start from an initial guess of the root at  <a href="https://www.codecogs.com/eqnedit.php?latex=x_0" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_0" title="x_0" /></a> and iteratively generate our next guess <a href="https://www.codecogs.com/eqnedit.php?latex=x_n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_n" title="x_n" /></a> in the following way.
2. We follow the function (blue curve) along its local tangent at  <a href="https://www.codecogs.com/eqnedit.php?latex=x_n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_n" title="x_n" /></a> and extrapolate a line towards y = 0. If the function is linear then we are done! But in general the function is not, so we are brought to  <a href="https://www.codecogs.com/eqnedit.php?latex=x_{n+1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{n+1}" title="x_{n+1}" /></a>, which is an improvement, since we are moving closer to the real zero. The value of  <a href="https://www.codecogs.com/eqnedit.php?latex=x_{n+1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{n+1}" title="x_{n+1}" /></a>  can be calculated from basic geometry: 
<a href="https://www.codecogs.com/eqnedit.php?latex=x_{n&plus;1}=x_{n}-{f(x_n)}/{f'(x_n)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_{n&plus;1}=x_{n}-f(x_n)/f'(x_n)" title="x_{n+1}=x_{n}-{f(x_n)}/{f'(x_n)}" /></a>.

3. We iterate this process until the change in our estimate is smaller than a certain threshold. All figures from wikipedia https://en.wikipedia.org/wiki/Newton%27s_method

<a title="Ralf Pfeifer, CC BY-SA 3.0 &lt;http://creativecommons.org/licenses/by-sa/3.0/&gt;, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:NewtonIteration_Ani.gif"><img width="512" alt="NewtonIteration Ani" src="https://upload.wikimedia.org/wikipedia/commons/e/e0/NewtonIteration_Ani.gif"></a>

Complete the function newton1() following the recipe above. The algorithm will require the user to provide both the function and its first derivative, as well as a starting guess. Test your Newton-Raphson function on a sine function and demonstrate finding a root near x = pi. We will provide the sine function along with its derivative - a cosine function.
