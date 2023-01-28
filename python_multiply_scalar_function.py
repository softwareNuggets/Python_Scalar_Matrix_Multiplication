from array import *
from typing import List


def multiply(s: int, A: List[int]) -> List[int]:

    # r x c  example, A below is a 3 x 3
    
    rows = len(A)
    cols = len(A[0])

    #The _ in the for _ in statement is a common convention
    #for indicating that the loop variable is not used. It is
    #a way to indicate that the loop variable is being used
    #only for the side effect of the loop, for example
    #for indexing, and not for any other purpose.
    
    matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    
    
    for r in range(rows):
        for c in range(cols):
            matrix[r][c] = s * A[r][c]

    return matrix



#A Matrix
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

R = multiply(5,A)



print(A, end='\n\n')
print(R, end='\n\n')






