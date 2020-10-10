import numpy as np
import scipy.optimize as opt
correlation = np.array([[1.0, 0.39, 0.53, 0.37, 0.01], [0.39, 1.0, -0.14, 0.37, -0.08], [
                       0.53, -0.14, 1.0, -0.16, 0.17], [0.37, 0.37, -0.16, 1.0, -0.39], [0.01, -0.08, 0.17, -0.39, 1.0]])
stand_devaition = np.array([0.023, 0.020, 0.037, 0.063, 0.12])
cov_panth = []
for i in range(len(stand_devaition)):
    for j in range(len(stand_devaition)):
        cov_panth = cov_panth + [correlation[i, j]
                                 * stand_devaition[i]*stand_devaition[j]]
cov_panth = np.array(cov_panth)
cov_panth = cov_panth.reshape(5, 5)

print(cov_panth**2.-1.)


