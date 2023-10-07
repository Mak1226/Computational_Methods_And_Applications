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
                sum = self.vector[i] + rv.vector[i]
                ans.append(sum)
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


# Sample Test 1
r = RowVectorFloat([1, 2 , 4])
print(r)
print(len(r))
print(r[1])
r[2] = 5   
print(r)

# Sample Test 2
r = RowVectorFloat([])
print(len(r))

# Sample Test 1
r1 = RowVectorFloat([1, 2, 4])
r2 = RowVectorFloat([1, 1, 1])
r3 = 2 * r1 + (-3) * r2
print(r3)