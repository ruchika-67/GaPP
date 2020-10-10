import numpy as np
data = np.loadtxt("zthetasigma.dat")

z= data[:,0]
theta=data[:,1]
sigma_theta = data[:,2]
rd= 147.5

D_A=[]
sigma_DA= []
print(len(z))

for i in range(len(z)):
   D_A1 = rd/((1+z[i])*0.0174533*theta[i])
   sigma_DA1 = D_A1 * (sigma_theta[i] / theta[i])
   D_A.extend([D_A1])
   sigma_DA.extend([sigma_DA1])

#np.savetxt('da.txt',D_A,delimiter=' ', fmt='%f')
ac=np.c_[z,D_A]
ad=np.c_[ac,sigma_DA]
np.savetxt('z_DA.txt',ad,delimiter=' ', fmt='%f')
