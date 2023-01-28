import numpy as np;

def print_header(title,width):
    print('|'+title.center(width,'*')+'|')


#the scalar value
#remember, a scalar value is simply a single real number
SCALAR = 4;

    
#A Matrix
A = np.array(   [[-3,5,6],
                 [1,7,8]], dtype=int)
# r,c = 2x3 matrix


print_header('np.multiply() 2x3',60)

R = np.multiply(A,SCALAR)

print(A, end='\n\n')
print(SCALAR, end='\n\n')
print(R, end='\n\n')


print_header('np.multiply()',60)

R2 = np.multiply(SCALAR,A)

print(A, end='\n\n')
print(SCALAR, end='\n\n')
print(R2, end='\n\n')
