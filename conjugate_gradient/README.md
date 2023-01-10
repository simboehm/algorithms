# Optimizing Functions with Conjugate Gradient in scipy.optimize.minimize

## Overview
Conjugate gradient is an algorithm used to find the minimum of a function. It is particularly useful for finding the minimum of a function that is defined by a large number of variables, such as in machine learning.

The algorithm works by iteratively improving an approximation to the minimum of the function. At each step, the algorithm computes a direction in which the function is decreasing the fastest, and moves in that direction. The direction is chosen to be "conjugate" to the previous direction, meaning that it is perpendicular to all the previous directions. This helps the algorithm converge faster, because it avoids oscillating back and forth between different directions.

The algorithm stops when it reaches a point where the function is no longer decreasing, or when the improvement in the approximation is below a certain threshold.

Overall, conjugate gradient is a fast and efficient algorithm for finding the minimum of a function, and is widely used in a variety of applications, including machine learning, optimization, and scientific computing.

## Usage
Conjugate gradient is an algorithm for finding the minimum of a differentiable, real-valued function $f(x)$, defined over an n-dimensional domain. The algorithm works by iteratively constructing a sequence of n-dimensional search directions $p_k$, and using these directions to generate a sequence of points $x_k$ that approximates the minimum of the function.

At each iteration, the algorithm computes the gradient of the function at the current point, $g_k = \nabla f(x_k)$, and uses this to compute the next search direction $p_k$ as a linear combination of the previous search direction $p_{k-1}$ and the gradient $g_k$. Specifically, $p_k$ is chosen to be conjugate to all the previous search directions $p_0, p_1, ..., p_k-1$, meaning that it is orthogonal to all of these directions. This is done to ensure that the algorithm does not oscillate back and forth between different directions, and converges more quickly to the minimum of the function.

The search direction $p_k$ is then used to generate the next point $x_{k+1}$ by moving a small distance in the direction of $p_k$. This is done using a line search algorithm, which determines the optimal step size $\alpha_k$ that minimizes the function in the direction of $p_k$. The new point $x_{k+1}$ is then computed as $x_{k+1} = x_k + \alpha_k p_k$.

The algorithm stops when the gradient of the function at the current point is close to zero, indicating that the minimum of the function has been found to a satisfactory accuracy. The conjugate gradient algorithm has a number of attractive properties, including a global convergence guarantee and a low per-iteration computational cost. It is widely used in a variety of applications, including machine learning, optimization, and scientific computing.

## Example
Here is a short example of using the conjugate gradient algorithm to minimize a quadratic function using the scipy.optimize.minimize function:

```python
import numpy as np
from scipy.optimize import minimize

# Define the quadratic function to minimize
def quadratic(x):
    return (x[0] - 2) ** 2 + (x[1] - 3) ** 2


# Initialize the optimization at x = [0, 0]
x0 = np.array([0, 0])

# Use the conjugate gradient algorithm to minimize the function
res = minimize(quadratic, x0, method="CG")

# Print the optimal point found by the algorithm
print(res.x)
```

This code will find the minimum of the quadratic function, which is at the point [2, 3]. The output of the minimize function will contain the optimal point found by the algorithm, as well as other information about the optimization process.
