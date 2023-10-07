import math
import matplotlib.pyplot as mpl

# Calculating factorial using the formula:
# n! = sqrt(2*pi*n) * (n/e)^n

# Calculating factorial using log method
def factorial(n):
    log = [0]
    for i in range (2 , n):
        log.append(log[-1] + math.log10(i))                 #  log(n!) = log((n-1)!) + log(n) 
    return log

# Function to calculate the approximation using Sterling's Formula

def formula(n):
    a = 0.5 * (math.log10(2) + math.log10(math.pi) + math.log10(n))
    b = n * (math.log10(n) - math.log10(math.e))
    return a + b

axis = range(1 , 1000000)
x = [formula(i) for i in axis]
y = factorial(1000000)

# Defining the attributes to plot graph

mpl.title("Visualisation of Stirling's approximation" , loc='center')
mpl.xlabel("n")
mpl.ylabel("Log10(n!)")
mpl.plot(axis, y , color = 'r', label="Log of Factorial")
mpl.plot(axis, x , linestyle='dashed', color = 'b' , label="Log of Stirling approximation")
mpl.legend()
mpl.show()
