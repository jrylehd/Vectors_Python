#<Josh Ryle> <Dimaculangan>
#MCS 260 Spring 2023 Project 3
#I hereby attest that I have adhered to the rules for projects as well as
#UIC’s Academic Integrity standards while completing this project.

class Vector():
    def __init__(self, P, Q):
        ''' The first two for loops are raising the initial type error when initiating the class Vector and making sure
        that the given P's and Q's are numerical values that are translated as points. '''
        for x in P:
            if type(x) not in [int, float]:
                raise TypeError("To create an object in the Vector class, both inputs must be lists of numeric values.")
                
        for x in Q:
            if type(x) not in [int, float]:
                raise TypeError("To create an object in the Vector class, both inputs must be lists of numeric values.")
                
        ''' This if statement raises the AssertionError for points that do not coexist in the same dimensions. '''        
        if len(P) != len(Q):
            raise AssertionError("The inputs P or Q have different lengths.")
        
        ''' Creating the initiation of the vector using the differences of the indeces of the points per dimension in 
        P and Q and creating a new list representing the vector. '''
        self.initial = P
        self.terminal = Q
        self.vector = []
        for i in range(len(self.initial)):
            Y = self.terminal[i] - self.initial[i]
            self.vector.append(Y)

    def dim(self):
        ''' Finds the length of a single vector. '''
        return len(self.vector)

    def __str__(self):
        ''' This takes the values in the vector self.vector and converts those values to strings inside of the list
        vector_string. '''
        vector_string = []
        for x in self.vector:
            vector_string.append(str(x))

        ''' Then, the string is made into how we view vectors in textbooks and conjoins them with the arrowed brackets
        and separates each x in the list vector_string by commas. '''
        string =  ",".join(vector_string)
        return "<" + string + ">"

    def __setitem__(self, i, z):
        if i >= self.dim():
            raise AssertionError("Index is out of bounds.")
        self.vector[i-1] = z

    def __getitem__(self, i):
        if i >= self.dim():
            raise AssertionError("Index is out of bounds.")
            
        return self.vector[i-1]

    def __eq__(V, W):
        ''' This makes sure that the two vectors are not returned if their types are not both vectors. '''
        if type(V) != Vector or type(W) != Vector:
            return False

        ''' This makes sure that the two vectors are not returned if the lengths of them are not equal to each other. '''
        if V.dim() != W.dim():
            return False
        
        ''' This checks for the equality of two vectors and their elements. '''
        for x in range(V.dim()):
            if V.vector[x] != W.vector[x]:
                return False
            else:
                pass

        return True      

    def __add__(V, W):
        ''' If one or both of the "vectors" being added are not vectors, then the addition is not possible. '''
        if type(V) != Vector or type(W) != Vector:
            raise AssertionError("The input vectors are not all vectors.")

        ''' If the lengths of the vectors are equal, we can add their indeces and append those into a list, X.
        We then have to convert that list into a Vector object and return that Vector object. ''' 
        X = []
        if V.dim() == W.dim():
            for i in range(V.dim()):
                X.append(V.vector[i] + W.vector[i])
        
        ''' This is the process that turns the list, X, into a Vector object. '''
        D = Vector([0 for i in range(len(X))], X)

        return D

    def __sub__(V, W):
        ''' If one or both of the "vectors" being added are not vectors, then the subtraction is not possible. '''
        if type(V) != Vector or type(W) != Vector:
            raise AssertionError("The input vectors are not all vectors.")

        ''' If the lengths of the vectors are equal, we can add their indeces and append those into a list, X.
        We then have to convert that list into a Vector object and return that Vector object. ''' 
        X = []
        if V.dim() == W.dim():
            for i in range(V.dim()):
                X.append(V.vector[i] - W.vector[i])
            
        ''' This is the process that turns the list, X, into a Vector object. '''
        D = Vector([0 for i in range(len(X))], X)

        return D

    def __mul__(V, W):
        ''' If V and W are both vectors but the lengths are different, then the AssertionError will call that error. '''
        if type(V) == Vector and type(W) == Vector:
            if V.dim() != W.dim():
                raise AssertionError("The input vectors have different lengths.")

            ''' This takes the element in each vector and multiplies them with each other and adds them to the empty variable
            dot_product as it goes through each index in the vector. '''
            dot_product = 0
            for x in range(V.dim()):
                dot_product += V.vector[x]*W.vector[x]

            return dot_product

        # This takes into account scalar and vector multiplication in one way,
        # where each element in the vector is first being multiplied to the scalar.
        # Then we return that new scaled list of numbers as a vector.
        elif type(V) == Vector and type(W) in [int, float]:
            X = []
            for v in V.vector:
                y = v*W
                X.append(y)
                
            D = Vector([0 for i in range(len(X))], X)

            return D

    ''' Using __rmul__ takes the commutative way of multiplying the scalar with the vector since order doesn't matter. '''
    def __rmul__(V, W):
        if type(V) == Vector and type(W) in [int, float]:
            X = []
            for v in V.vector:
                z = W*v
                X.append(z)
                
            D = Vector([0 for i in range(len(X))], X)

            return D

    def __abs__(self):
        ''' We start with X = 0, and we found the sum of all the elements squared in self.vector.
        Once that process was finished, we took the square root of that X and renamed the new result as X.
        We then rounded it to four decimales as asked. '''
        X = 0
        for v in self.vector:
            X += v**2
        
        X = X**0.5

        return round(X, 4)

def cross_product(V, W):
    ''' Only vectors of length 3 can be used for this cross product method. '''
    if V.dim() == 3 and (V.dim() == W.dim()):
        ''' This is how it should essentially look like when doing cross productts:
        Reference: < d2e3 − d3e2, d3e1 − d1e3, d1e2 − d2e1 > '''
        X = [(V.vector[1] * W.vector[2]) - (V.vector[2] * W.vector[1]), 
             (V.vector[2] * W.vector[0]) - (V.vector[0] * W.vector[2]), 
             (V.vector[0] * W.vector[1]) - (V.vector[1] * W.vector[0])
        ]
        
        D = Vector([0 for i in range(len(X))], X)
        return D   
    else:
        raise AssertionError("One or more input vectors do not have the correct lengths.")

def is_parallel(V, W):
    ''' If either V or W are not vectors, then this function does not work. '''
    if type(V) != Vector or type(W) != Vector:
        return False
    
    ''' If V or W are different length vectors, then they cannot be parallel. '''
    if V.dim() != W.dim():
        return False
    
    X = []
    for i in range(V.dim()):
        ''' If division by zeros are needed, then it cannot be parallel. '''
        if V.vector[i] == 0 and W.vector[i] == 0:
            return False
        
        ''' We take the higher scaled vector's absolute value and divide that by the smaller scaled vector's absolute value
        and append those values into a list so that we can compare those scales with each other. '''        
        if abs(V.vector[i]) > abs(W.vector[i]):
            L = V.vector[i] / W.vector[i]
        elif abs(V.vector[i]) <= abs(W.vector[i]):
            L = W.vector[i] / V.vector[i]
        X.append(L)

    ''' This compares each element in X to the next element. If they are the same number,
    then that means that the higher scaled vector is parallel to the smaller scaled vector
    and that they were all multiplied by the same amount. '''
    for i in range(len(X)-1):
        if X[i] == X[i+1]:
            pass
        else:
            return False

    return True