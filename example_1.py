import numpy as np;

def print_header(title,width):
    print('|'+title.center(width,'*')+'|')


#the scalar value
#remember, a scalar value is simply a single real number
SCALAR = 6;

    
#A Matrix
A = np.array([[4,8,12]])
#r,c = 1x3



print_header('np.multiply()',60)


R = np.multiply(SCALAR,A)

print(A, end='\n\n')
print(SCALAR, end='\n\n')
print(R, end='\n\n')


print_header('np.multiply()',60)

R2 = np.multiply(A,SCALAR)

print(A, end='\n\n')
print(SCALAR, end='\n\n')
print(R2, end='\n\n')
