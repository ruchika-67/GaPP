import numpy as np
from scipy import linalg
a = np.array([[0.000529, 0.000179, 0.000451, 0.000536, 0.000028],[0.000179, 0.000400, -0.000104, 0.000466, -0.000192],[0.000451, -0.000104, 0.001369, -0.000373, 0.000755],[0.000536, 0.000466, -0.000373, 0.003969, -0.002948],[0.000028, -0.000192, 0.000755, -0.002948,0.014400]])
#ev= linalg.eigvals(a)
#print(ev)

evalue,evec = linalg.eig(a)
print(evalue,evec)

print(np.diag(a))

#test1= np.dot(a,evec)
#test2= np.dot(ev,evec)


#print(test1)
#print(test2)
