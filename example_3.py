import numpy as np;

def print_header(title,width):
    print('|'+title.center(width,'*')+'|')


    
#A Matrix
A = np.array(   [[4.0,  8.0,    12.0]])


print_header('np.multiply()',60)

SCALAR = (1/4);

R = np.multiply(A,SCALAR)

print(A, end='\n\n')
print(SCALAR, end='\n\n')
print(R, end='\n\n')

print_header('np.multiply()',60)

R2 = np.multiply(SCALAR,A)

print(A, end='\n\n')
print(SCALAR, end='\n\n')
print(R2, end='\n\n')
