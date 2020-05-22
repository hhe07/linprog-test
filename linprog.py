import numpy as np
from scipy.optimize import minimize

xvals = np.array([1.0,1.0,1.0,1.0,1.0])

def rev(x):
    return -1*(350 * x[0] + 475 * x[1] + 425 * x[2] + 500 * x[3] + 400 * x[4])



bounds = ((0, 6), (0, 6), (0, 6), (0, 6), (0, 6))
constr = ({"type": "ineq", "fun": lambda x: -1*(x[0]+x[1]+x[2]+x[3]+x[4])+12},
{"type": "ineq", "fun": lambda x: (30 * x[0] + 5 * x[1] + 25 * x[2]) - 150},
{"type": "ineq", "fun": lambda x: (30 * x[1] + 10 * x[4]) - 70},
{"type": "ineq", "fun": lambda x: (20 * x[0] + 30 * x[2]) - 200},
{"type": "ineq", "fun": lambda x: ((20 * x[0] + 30 * x[2] + 20 * x[3] + 10 * x[4] + 5*x[1]) - (30 * x[0] + 25 * x[2] + 30 * x[1] + 10 * x[4]))})
res = minimize(rev, xvals, method="SLSQP", constraints = constr, bounds = bounds)

print(res.x)