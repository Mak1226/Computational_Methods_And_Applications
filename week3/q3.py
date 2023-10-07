from random import uniform
import numpy as np
import matplotlib.pyplot as mpl


class RowVectorFloat:

    # method checks whether a value is of int or float datatype or not in a list
    def value(self, l):

        if isinstance(l,list):
            for i in l:
                if not isinstance(i, int) and not isinstance(i, float):
                    raise Exception(f"Invalid value recieved.")
        
        else:
            raise Exception(f"Invalid Input")

        return 1

    # method checks whether a valid index is given as a argument or not
    def index(self, ind):

        if isinstance(ind, int):
            if ind not in range(len(self.vector)):
                raise Exception(f"Index out of bound.")
                
        else:
            raise Exception(f"Invalid index received.")
        
        return 1

    # constructor to initialize the values of the list
    def __init__(self, l):

        if self.value(l):
            self.vector = list(l)

    # method returns row vector in string format
    def __str__(self):

        s=[]
        for i in self.vector:
            if not isinstance(i,float):
                s.append(str(i))    
            else:
                s.append(f"{i:.3f}")

        return " ".join(s)

    # method returns length of the vector    
    def __len__(self):
        size = len(self.vector)
        return size

    # method returns value at the index
    def __getitem__(self, ind):

        if self.index(ind):
            val = self.vector[ind]
            return val

    # method sets the value at the given index
    def __setitem__(self, ind, val):

        if self.value([val]) and self.index(ind):
                self.vector[ind] = val

    # method adds 2 row vector
    def __add__(self, rv):

        if len(self.vector) == len(rv.vector) and isinstance(rv,RowVectorFloat):
            ans=[]
            for i in range(len(self.vector)):
                s = self.vector[i] + rv.vector[i]
                ans.append(s)
            return RowVectorFloat(ans)

        else:
            if not isinstance(rv, RowVectorFloat):
                raise Exception("The Given vector is of different instance")
            elif len(self.vector) != len(rv.vector):
                raise Exception("The given vector has different lengths")

    # incase of right hand side addition we will call ___add__ by passing new vector as argument
    def __radd__(self, rv):

        return self.__add__(rv)

    # method multiplies vector with a scalar value
    def __mul__(self, num):

        ans=[]
        if isinstance(num, (int, float)):
            for i in range(len(self.vector)):
                pro = num * self.vector[i]
                ans.append(pro)
            return RowVectorFloat(ans)  
        raise Exception("Expected a scalar value")

    # incase of a right hand side multiplication, we will call __mul__ by passing scalar as argument
    def __rmul__(self, num):

        return self.__mul__(num)

class SquareMatrixFloat:

    # constructor to initialize the square matrix
    def __init__(self, num):

        if isinstance(num, int):
            self.n = num
            self.mat=[]
            for i in range(num):
                for j in range(num):
                    row = RowVectorFloat([0] * num)
                self.mat.append(row)

        else:
            raise Exception("Invalid input - Expected int")

    # method return the square matrix as a string
    def __str__(self):
        
        print("The Matrix is\n")
        ans=""
        for i in range(self.n):
            p = str(self.mat[i])
            ans = ans + p + "\n"
        return ans

    # method to sample a random symmetric matrix
    def sampleSymmetric(self):
        
        for i in range(self.n):
            for j in range(i):
                self.mat[i][j] = uniform(0, 1)
                self.mat[j][i] = self.mat[i][j]
            self.mat[i][i] = uniform(0, self.n)

    # methid that will convert the matrix into its Row Echelon form
    def toRowEchelonForm(self):
        
        r=0
        c=0
        while True:
            if r >= self.n or c >= self.n:
                nz = r
                while True:
                    if nz >= self.n or self.mat[nz][c] != 0:
                        nz += 1

                    else:
                        break

                if nz == self.n:
                    c = c + 1
                    continue

                if nz != r:
                    t = self.mat[nz]
                    self.mat[nz] =  self.mat[r]
                    self.mat[r] = t

                self.mat[r][c] = 1.00
                val = np.reciprocal(self.mat[r][c])
                self.mat[r] *= val

                for i in range(r + 1, self.n):
                    if self.mat[i][c] != 0:
                        self.mat[i][c] = 0.00
                        d = self.mat[r] * -self.mat[i][c]
                        self.mat[i] += d

                r = r + 1
                c = c + 1

            else:
                break

        return self

    # method to check whether a matrix is diagonally row dominant or not
    def isDRDominant(self):

        for i in range(self.n):
            s = 0
            for j in range(self.n):
                if i != j:
                    s += self.mat[i][j]
                else:
                    d = self.mat[i][j]
            if d <= s:
                return False
        return True

    # method checks whether value is valid or not
    def value(self, l):

        if isinstance(l,list):
            for i in l:
                if not isinstance(i, int) and not isinstance(i, float):
                    raise Exception(f"Invalid value recieved.")
        
        else:
            raise Exception(f"Invalid Input")

        return 1

    # Function to find the value for each iteration
    def itrn(self, b, m, jk):
            
        if not isinstance(m, int) or m < 0:
            raise Exception(f"Enter a positive integer")
        if not self.isDRDominant() and jk is True:
            raise Exception("Not solving because convergence is not guranteed.")

        if self.value(b):
            A = [[self.mat[i][j] for j in range(self.n)] for i in range(self.n)]
            A = np.array(A)

            pre,x,er = [],[],[]
            
            for i in range(self.n):
                pre.append(0)
                x.append(0) 

            for i in range(m):
                for j in range(self.n):
                    s = 0
                    for k in range(self.n):
                        if j == k:
                            continue

                        elif jk == False and k < j:
                            s += self.mat[j][k] * x[k]
                        
                        else:
                            s += self.mat[j][k] * pre[k]
                        
                    v = (b[j] - s)
                    x[j] = v / self.mat[j][j]

                k = np.linalg.norm(A @ np.array(x) - np.array(b))
                er.append(k)
                
                pre = list(x)
                
            ans = list(pre)

            return (er, ans)

    # method performs m iterations on Jacobi formula
    def jSolve(self, b, m):
        
        return self.itrn(b, m, jk=1)

    # method performs m iterations on Gauss-Siedel formula
    def gsSolve(self, b, m):
        
        return self.itrn(b, m, jk=0)

    # method to display/visualize the graph of Jacobi and Gauss-Siedel methods
    def graph(self):

        self.sampleSymmetric()
        while not self.isDRDominant():
            self.sampleSymmetric()

        itr = 50  # Number of iterations
        b = list(range(self.n))  

        # Using Jacobi method
        je, jx = self.itrn(b, itr, jk=1)

        # Using Gauss-Siedel method
        gse, gsx = self.itrn(b, itr, jk=0)

        x=[]
        for i in range(1,itr+1):
            x.append(i)

        # Plotting the rate of convergence
        mpl.title(f"Rate of convergence of Jacobi and Gauss-Siedel methods\n({itr} iterations, {self.n}x{self.n} matrix)")
        mpl.plot(x, je, c="b", label="Jacobi Method")
        mpl.plot(x, gse, c="r", label="Gauss-Siedel Method")
        mpl.xlabel("Number of Iterations")
        mpl.ylabel("Error : ||Ax⁽ᵏ⁾ - b||₂")
        mpl.grid()
        mpl.legend()
        mpl.show()


# Sample Test Case
s = SquareMatrixFloat(10)
s.graph()