import numpy as np
from scipy.optimize import minimize

xvals = np.array([1.0, 1.0, 1.0, 1.0, 1.0])  # Starting values for each of the variables: the size of the array (e.g. how many variables the equation has) is dependendent on length of array
# For example, the above has size 5.

def rev(x):
    return -1*(350 * x[0] + 475 * x[1] + 425 * x[2] + 500 * x[3] + 400 * x[4])
# The solver requires one to pass in a cost function taking a array-like entity x. Since SciPy only does minimisation -1 is required to change to maximising


bounds = ((0, 6), (0, 6), (0, 6), (0, 6), (0, 6)) # Each of these tuples is min, max bounds for each variable in order.
constr = ({"type": "ineq", "fun": lambda x: -1*(x[0]+x[1]+x[2]+x[3]+x[4])+12},
{"type": "ineq", "fun": lambda x: (30 * x[0] + 5 * x[1] + 25 * x[2]) - 150},
{"type": "ineq", "fun": lambda x: (30 * x[1] + 10 * x[4]) - 70},
{"type": "ineq", "fun": lambda x: (20 * x[0] + 30 * x[2]) - 200},
{"type": "ineq", "fun": lambda x: ((20 * x[0] + 30 * x[2] + 20 * x[3] + 10 * x[4] + 5 * x[1]) - (30 * x[0] + 25 * x[2] + 30 * x[1] + 10 * x[4]))})
# The above unit of a tuple is a tuple of dictionaries, each containing the type (ineq), and the function to get the processed variable for the evaluation.
# They're designed to be x>=0, e.g. the lambda evaluation is supposed to be greater than zero. They're all rewritten to do so.
res = minimize(rev, xvals, method="SLSQP", constraints = constr, bounds = bounds)
# Just picked whatever method allowed bounds.
print(res.x)