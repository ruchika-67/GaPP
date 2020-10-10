import sympy 
from sympy import * 
import numpy as np





M= Matrix([[Rational(529,1000000), Rational(179,1000000), Rational(451,1000000), Rational(67,125000), Rational(7,250000)],
 [Rational(179,1000000), Rational(1,2500), Rational(-13,125000), Rational(233,500000), Rational(-3,15625)],
 [Rational(451,1000000), Rational(-13,125000), Rational(1369,1000000), Rational(-373,1000000), Rational(151,200000)], 
[Rational(67,125000), Rational(233,500000), Rational(-373,1000000), Rational(3969,1000000), Rational(-737,250000)],
 [Rational(7,250000), Rational(-3,15625), Rational(151,200000), Rational(-737,250000), Rational(9,625)]])
#np.savetxt('temp2.txt', M1, fmt='%f')

print("Matrix : {} ".format(M)) 
   
# Use sympy.diagonalize() method  
P, D = M.diagonalize()   
      
print("Diagonal of a matrix : {}".format(D)) 
