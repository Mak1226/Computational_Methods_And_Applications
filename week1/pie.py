import random
import matplotlib.pyplot as mpl
 
def estimatePi(n):
    circle = square = 0
    pi = []
    axis = []
    estm = []

    for i in range(n):
        pi.append(3.14)
        axis.append(i)
        square += 1
        
        # Selecting a random point
        x = random.uniform(-1 , 1 )
        y = random.uniform(-1 , 1)

        # Checking whether point lies within the circle or not
        if pow(x,2) + pow(y,2) <= 1 :
            circle += 1

        # Calcualting the value of [4 * (Points in circle/Points in square)]
        valuePi = 4 * float(circle)/float(square)
        estm.append(valuePi)

    # defining the attributes to plot graph

    mpl.title("Estimating pi using Monte Carlo Method")
    mpl.xlabel("No. of points generated")
    mpl.ylabel("4 * fraction of points within the circle")
    mpl.ylim(3.1,3.4)
    mpl.plot(axis , estm, label = "Monte Carlo method" , color = 'b') 
    mpl.plot(axis , pi, label = "Value of math.pi" , color = 'r')
    mpl.legend()
    mpl.show()
    return estm


estimatePi(200000)
        
        
