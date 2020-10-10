import numpy as np
data = np.loadtxt("zthetasigma.dat")

z= data[:,0]
theta=data[:,1]
sigma_theta = data[:,2]
rd= 147.5

D_Abyrd=[]
sigma_DAbyrd= []
print(len(z))

for i in range(len(z)):
   D_A1byrd = 1./((1+z[i])*0.0174533*theta[i])
   sigma_DA1byrd = D_A1byrd * (sigma_theta[i] / theta[i])
   D_Abyrd.extend([D_A1byrd])
   sigma_DAbyrd.extend([sigma_DA1byrd])

#np.savetxt('da.txt',D_A,delimiter=' ', fmt='%f')
ac=np.c_[z,D_Abyrd]
ad=np.c_[ac,sigma_DAbyrd]
np.savetxt('z_DAbyrd.txt',ad,delimiter=' ', fmt='%f')
