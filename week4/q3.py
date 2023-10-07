import matplotlib.pyplot as mpl
import numpy as np

# method to calculate sin (x^2) of each value
def fun(x):
    return np.sin(np.power(x,2))

# method to calculate 1st derivative
def derv(x):
    return 2 * x * np.cos(np.power(x,2))

# method to calculate 2nd derivative
def derv2(x):
    p = np.power(x,2)
    a = 2 * np.cos(p)
    b = 4 * p * np.sin(p)
    return a - b

# method to calculate 3rd derivative
def derv3(x):
    p = np.power(x,2)
    a = -12 * x * np.sin(p)
    b = -8 * x * p * np.cos(p)
    return a + b

# method to calculate the forward and centred finite diff approx
def cal(x, h, f):
    a = x+h
    if f:
        b = x - h
        c = h
    else:
        b = x
        c = 2 * h
    return ((fun(a) - fun(b)) / c)

# method to plot the calculate
def graph(h,a,b,c,d,e):
    mpl.title(f"Absolute error of approx for \n δ⁺(x), δ⁻(x) and δᶜ(x) of {e}")
    mpl.xlabel("h  →")
    mpl.ylabel("Maximum absolute error  →")
    mpl.plot(h, d, c="y", label="Theoretical centered approx")
    mpl.plot(h, b, c="b", label="Theoretical forward approx")
    mpl.plot(h, c, c="g", label="Centered approx")
    mpl.plot(h, a, c="r", label="Forward approx")
    mpl.grid()
    mpl.legend()
    mpl.show()

# method to calculate the absolute errors of the approximations
def calculate(mn, mx, p):
    s= "sin(x^2)"
    # Set the number of points to plot
    x = np.linspace(mn, mx, p)

    # Only appending the non zero values
    h = []
    for i in x:
        if i:
            h.append(i)
            
    fae, cae, tfe, tce = [], [], [], []

    # Compute the error for each value of h using both methods
    for i in h:
        mfe = mtf = mce = mtc = 0

        for j in np.linspace(mn, mx, p):

            # for forward approx
            val = np.absolute(cal(j, i, True) - derv(j))
            mfe = np.maximum(mfe, val)
            d2, d3 = 0, 0

            for k in np.linspace(j, j + i, p):
                val = np.absolute(derv2(k))
                d2 = np.maximum(d2, val)
                val = np.absolute(derv3(k))
                d3 = np.maximum(d3, val)
            
            val = (i / 2) * d2
            mtf = np.maximum(mtf, val)

            # for centered approx
            val = np.absolute(cal(j, i, False) - derv(j))
            mce = np.maximum(mce, val)
            val = (i * i / 6) * d3
            mtc = np.maximum(mtc, val)

        # Append the max absolute and theoretical errors for each value of h
        fae.append(mfe)
        tfe.append(mtf)
        cae.append(mce)
        tce.append(mtc)

    graph(h, fae, tfe, cae, tce, s)

calculate(0, 1, 100)

