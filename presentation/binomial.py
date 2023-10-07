import numpy as np
import matplotlib.pyplot as mpl
import math

def integration(n):
    x = 0.5
    value = x / (2 * n + 1)
    return value


def binomial_series(n, x, t):
    terms = []
    terms.append(1)

    for r in range(1, t):
        coefficient = 1
        for k in range(r):
            coefficient *= (n - k)

        fact = (int(math.factorial(r)))
        coefficient /= fact
        coefficient = coefficient * np.power((-1) * np.power(x, 2), r)
        terms.append(coefficient)

    return terms


def graph(t, p):
    mpl.title("Value of π")
    mpl.axhline(y=np.pi, color="g", label="Actual π")
    mpl.plot(t, p, color="r", label="Simulated π value")

    mpl.grid()
    mpl.legend()
    mpl.show()


def graph_error(t,e):
    mpl.title("Error in π")
    # mpl.axhline(y=np.pi, color="g", label="Actual π")
    mpl.plot(t, e, color="r", label="error")

    mpl.grid()
    mpl.legend()
    mpl.show()

def compute_pi(no_of_terms):
    series_coefficient = binomial_series(0.5, 0.5, no_of_terms)
    new_series = []
    sum = 0

    for i in range(no_of_terms):
        value = series_coefficient[i] * integration(i)
        new_series.append(value)
        sum += value

    constant = np.power(3, 0.5)/8
    evaluated_pi = 12 * (sum - constant)

    return evaluated_pi
    # print(f"computed: {evaluated_pi} \nactual  : {np.pi}")


def simulate():
    pi, error_in_pi = [], []
    terms = np.linspace(1, 50, 50, dtype=int)

    for i in terms:
        pi_value = compute_pi(i)
        pi.append(pi_value)
        error_in_pi.append(pi_value - np.pi)

    # print(f"computed: {pi[-1]}")
    # print(f"computed: {error_in_pi[-1]}")
    # graph(terms, pi)
    graph_error(terms,error_in_pi)

simulate()