import random
import numpy as np
import matplotlib.pyplot as mpl

class Dice:

    def __init__(self, side = 6):

        self.side  = side

        # raises exception incase sides < 4 or sides not of int datatype
        if side < 4:
            raise Exception("<class 'Exception'>\nCannot construct the dice")
        if not isinstance(side , int):
            raise Exception("<class 'Exception'>\nCannot construct the dice")
        
        #Probability Distribution when not mention
        k = 1.0/float(self.side)
        self.prob = [k] * side                  

    # Printing object
    def __str__(self ):
        return f'Dice with {self.side} faces and probability distribution {tuple(self.prob)}'.replace('(' , '{').replace(')' , '}')
    
    def setProb(self , newProb ):
        if len(newProb) != self.side or sum(newProb) != 1:
            raise Exception("<class 'Exception'>\nInvalid probability distribution")

        self.prob = list(newProb)
    
    def roll(self , throw):

        exp = []
        fq = []
        x_axis = []
        
        for i in range(self.side):
            exp.append(0)
            fq.append(0)

        # Expected result
        for i in range(self.side):
            valExp = throw * self.prob[i]
            exp[i] = valExp

        for i in range(self.side):
            x_axis.append(i+1)
            p = self.prob[i] * 10
            self.prob[i] = p

        # Simulated result
        for i in range(throw):
            tmp = random.choices(range(0 ,  self.side , 1) , weights=self.prob , k=1)
            fq[tmp[0]] = fq[tmp[0]]+1
            

        # defining the attributes to plot graph
        X = np.arange(len(x_axis))
    
        mpl.bar(X + 0.15, exp, label = 'Expected', width= 0.25, color = 'r')
        mpl.bar(X - 0.15, fq, label = 'Actual' , width = 0.25, color = 'b')
        
        mpl.legend()
        mpl.title(f'Outcome of {throw} throws of a {self.side}-faced dice')
        mpl.xticks(X, x_axis)
        mpl.ylabel("Occurrences")
        mpl.xlabel("Sides")
        mpl.show()

# Test Case
d = Dice()
d.setProb((0.1, 0.17, 0.23, 0.15, 0.18, 0.17))
d.roll(10000)
print(d)
