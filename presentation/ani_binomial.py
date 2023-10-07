import numpy as np
import matplotlib.pyplot as mpl
import math
from matplotlib.animation import FuncAnimation as an
from decimal import Decimal, getcontext
getcontext().prec = 30


def integration(n):
    x = Decimal('0.5')
    value = Decimal(x) / (Decimal('2') * Decimal(n) + Decimal('1'))
    return Decimal(value)


def binomial_series(n, x, t):
    terms = []
    terms.append(Decimal('1'))

    for r in range(1, t):
        coefficient = Decimal('1')
        for k in range(r):
            coefficient = Decimal(coefficient) * (Decimal(n) - Decimal(k))

        fact = Decimal(math.factorial(r))
        coefficient = Decimal(coefficient) / Decimal(fact)
        coefficient = Decimal(coefficient) * \
            ((Decimal('-1') * (Decimal(x) ** 2)) ** r)
        terms.append(Decimal(coefficient))

    return terms


def graph(t, p):

    fig,axes = mpl.subplots(figsize=(20, 15))
    axes.set_title("Value of π")
    axes.axhline(y=np.pi,color="g",label="Actual π")
    axes.grid()

    def animate(i):
        if i==0:
            axes.legend(loc=1)
        axes.plot(t[:i],p[:i],color="r",label="Simulated π")

    ani = an(fig, animate, interval=300,frames=100,repeat=False)
    mpl.show()

def graph_error(t, e):
    
    fig,axes = mpl.subplots(figsize=(20, 15))
    axes.set_title("Error in π")
    # axes.axhline(y=np.pi,color="g",label="Actual π")
    axes.grid()

    def animate(i):
        if i==0:
            axes.legend(loc=1)
        axes.plot(t[:i],e[:i],color="r",label="error")
        axes.set_data(t[i],e[i])

    ani = an(fig, animate, interval=300,frames=100,repeat=False)
    mpl.show()

def compute_pi(no_of_terms):
    series_coefficient = binomial_series(
        Decimal('0.5'), Decimal('0.5'), no_of_terms)
    new_series = []
    sum = Decimal('0')

    for i in range(no_of_terms):
        value = Decimal(series_coefficient[i]
                        * Decimal(integration(Decimal(i))))
        new_series.append(Decimal(value))
        sum = Decimal(sum) + Decimal(value)

    constant = Decimal(3) ** Decimal('0.5') / Decimal('8')
    evaluated_pi = Decimal('12') * (Decimal(sum) - Decimal(constant))

    return evaluated_pi


def simulate():
    pi, error_in_pi = [], []
    terms = np.linspace(1, 50, 50, dtype=int)
    value_of_pi = Decimal('3.141592653589793238462643383279')

    for i in terms:
        pi_value = compute_pi(i)
        pi.append(pi_value)
        error_in_pi.append(pi_value - value_of_pi)

    # print(f"computed: {pi[-1]}")
    # print(f"error: {error_in_pi[-1]}")
    graph(terms, pi)
    # graph_error(terms, error_in_pi)


simulate()
