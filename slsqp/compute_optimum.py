import numpy as np
import plotly.graph_objects as go

from random import uniform
from scipy.optimize import minimize


# Define a function to return the value of a 3D parabola
def parabola(x, y):
    return x**2 + y**2


""" What is an objective function?
An objective function is a function that is used to evaluate the performance of a model or a set of parameters. 
It is often used in optimization algorithms to determine the optimal parameters that minimize or maximize the objective function.
By using an objective function in scipy.optimize, you can use optimization algorithms such as minimize() or curve_fit() 
to find the optimal parameters that minimize or maximize the objective function.
"""

# Define an objective function used by scipy.optimize.minimize
def objective_function(inputs):
    x, y = inputs
    return parabola(x, y)


""" What is a callback function?
In scipy.optimize.minimize you can use the callback argument to specify a function (callback function) 
that is called at each iteration of the optimization. The callback function can be used to store the current set of parameters 
and the corresponding objective function value at each iteration.
"""

# Define the callback function
def callback(k):
    x_k.append(k[0])
    y_k.append(k[1])
    z_k.append(parabola(k[0], k[1]))


# Define the domain
X = Y = np.linspace(-10, 10, 100)
xGrid, yGrid = np.meshgrid(
    X, Y
)  # np.meshgrid() returns coordinate matrices from coordinate vectors
Z = parabola(xGrid, yGrid)

# Initialize lists to store optimization trace
x_k = []
y_k = []
z_k = []

# Set the options for the optimization
options = {"eps": 1e-4}

# Optimization algorithm
initial_guess = [
    uniform(-10, 10),
    uniform(-10, 10),
]  # initial guess for the optimum
result = minimize(
    objective_function,
    initial_guess,
    method="SLSQP",
    options=options,
    callback=callback,
)

# result.x contains the optimal values for x and y (alternative: use x_k[-1] and y_k[-1])
x_opt, y_opt = result.x

# Create a figure
fig = go.Figure()

# Add a surface trace
fig.add_trace(
    go.Surface(
        x=X, y=Y, z=Z, colorscale="Viridis", lighting=dict(diffuse=1), opacity=0.5
    )
)

# Add a scatter3d trace (iteration steps and optimum)
fig.add_trace(
    go.Scatter3d(
        x=x_k,
        y=y_k,
        z=z_k,
        mode="markers+lines",
        marker=dict(size=5, color="red", symbol="circle"),
        line=dict(color="red", width=2),
    )
)

# Add a multi-line title to the figure
fig.update_layout(
    title="$f(x,y)=x^2 + y^2$",
    scene=dict(xaxis_title="x", yaxis_title="y", zaxis_title="f(x,y)"),
)

# Show the figure
fig.show()
