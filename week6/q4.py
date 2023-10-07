import matplotlib.pyplot as mpl
import numpy as np
from scipy.integrate import solve_ivp as ivp

# method to plot the graph
def plot(mu, t, x):
    mpl.title(f"Van der Pol equation for Mu(u) = {mu}")
    mpl.xlabel("t")
    mpl.ylabel("x(t)")
    mpl.plot(t, x)
    mpl.grid()
    mpl.show()

# method to solve ode using forward euler method
def ODEsolve(mu, x0, t0, v0, T, p):
    # x0, t0 = 0, 0
    # v0 = 10
    # T = 200
    # p = 10000

    # method to return the derivates of system of diff. eqn.
    def derv(_, y):
        x, v = y
        val = mu * (1 - x * x) * v - x
        return [v, val]

    t = np.linspace(t0, T, p)

    # solving using the solve_ivp method of scipy library
    sol = ivp(fun=derv, t_span=[t0, T], y0=[x0, v0], t_eval=t)
    x = sol.y[0]

    # plotting
    plot(mu, t, x)

    # Time Period
    v1 = 0
    for i in range(p - 1, 0, -1):
        if x[i] > 0 or x[i - 1] < 0:
            continue
        else:
            v1 = i
            break

    v2 = -1
    for i in range(v1 - 1, 0, -1):
        if x[i] > 0 or x[i - 1] < 0:
            continue
        else:
            v2 = i
            break

    T = np.absolute(t[v1] - t[v2])
    print(f"Time period(T) of curve for Mu(u) = {mu} : {T:.3f}")

# Test Case
ODEsolve(2, 0, 0, 10, 200, 10000)
