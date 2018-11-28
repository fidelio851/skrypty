#!/usr/bin/python

from __future__ import division
from copy import deepcopy
import math

class Matrix(object):
    """
    Represent a matrix and allow for basic matrix operations to be done.
    """
    def __init__(self, X):
        """
        X - a list of lists, ie [[1],[1]]
        """
        #Validate that the input is ok
        self.validate(X)
        self.X = X

    def validate(self, X):
        """
        Validate that a given list of lists is a proper matrix
        X - a list of lists
        """
        list_error = "X must be a list of lists corresponding to a matrix, with each sub-list being a row."
        #Input must be a list
        if not isinstance(X, list):
            raise Exception(list_error)
        #All list elements must also be lists
        for i in xrange(0,len(X)):
            if not isinstance(X[i], list):
                raise Exception(list_error)

        #All rows must have equal length
        first_row_len = len(X[0])
        for i in xrange(0,len(X)):
            if len(X[i])!=first_row_len:
                raise Exception("All rows in X must be the same length.")

    def invert(self):
        """
        Invert the matrix in place.
        """
        self.X = invert(self.X)
        return self
    
    @property
    def rows(self):
        """
        Number of rows in the matrix
        """
        return len(self.X)
    
    @property
    def cols(self):
        """
        Number of columns in the matrix
        """
        return len(self.X[0])
    
    def transpose(self):
        """
        Transpose the matrix in place.
        """
        trans = []
        for j in xrange(0,self.cols):
            row = []
            for i in xrange(0,self.rows):
                row.append(self.X[i][j])
            trans.append(row)
        self.X = trans
        return self

    def __getitem__(self, key):
        """
        Get a row of the matrix, ie m=Matrix([[1],[1]]); m[0]
        """
        return self.X[key]

    def __setitem__(self, key, value):
        """
        Set a row of the matrix, ie m=Matrix([[1],[1]]); m[0] = [2]
        """
        assert self.cols == len(value)
        self.X[key] = value

    def set_column(self, key, value):
        """
        Set a column to a specific value
        """
        assert self.rows == len(value)
        for i in xrange(0,self.rows):
            self.X[i][key] = value[i]

    def __delitem__(self, key):
        """
        Delete a row of the matrix
        """
        del self.X[key]

    def del_column(self, key):
        """
        Delete a specified column
        """
        for i in xrange(0,self.rows):
            del self.X[i][key]

    def __len__(self):
        """
        Get the length of the matrix
        """
        return self.rows

    def __rmul__(self, Z):
        """
        Right hand multiplication, ie other_matrix * matrix
        """
        #Only 2 Matrix objects can be multiplied
        assert(isinstance(Z, Matrix))

        #Number of columns in other matrix must match number of rows in this matrix
        assert Z.cols==self.rows

        product = []
        for i in xrange(0,Z.rows):
            row = []
            for j in xrange(0,self.cols):
                row.append(row_multiply(Z.X[i], [self.X[m][j] for m in xrange(0,self.rows)]))
            product.append(row)
        return Matrix(product)

    def __mul__(self, Z):
        """
        Left hand multiplication, ie matrix * other_matrix
        """
        assert(isinstance(Z, Matrix))

        assert Z.rows==self.cols

        product = []
        for i in xrange(0,self.rows):
            row = []
            for j in xrange(0,Z.cols):
                row.append(row_multiply(self.X[i], [Z[m][j] for m in xrange(0,Z.rows)]))
            product.append(row)
        return Matrix(product)

    def __str__(self):
        """
        String representation of matrix.
        """
        return str(self.X)

    def __repr__(self):
        """
        Representation of the matrix
        """
        return str(self.X)


    def determinant(self):
        return recursive_determinant(self)


def recursive_determinant(X):
    """
    Find the determinant in a recursive fashion.  Very inefficient
    X - Matrix object
    """
    #Must be a square matrix
    assert X.rows == X.cols
    #Must be at least 2x2
    assert X.rows > 1

    term_list = []
    #If more than 2 rows, reduce and solve in a piecewise fashion
    if X.cols>2:
        for j in xrange(0,X.cols):
            #Remove i and j columns
            new_x = deepcopy(X)
            del new_x[0]
            new_x.del_column(j)
            #Find the multiplier
            multiplier = X[0][j] * math.pow(-1,(2+j))
            #Recurse to find the determinant
            det = recursive_determinant(new_x)
            term_list.append(multiplier*det)
        return sum(term_list)
    else:
        return(X[0][0]*X[1][1] - X[0][1]*X[1][0])

X = Matrix([[4,4,1],[0,4,3],[1,0,2]])
R = recursive_determinant(X)
print R
