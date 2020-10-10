import numpy as np
data= np.loadtxt("Hdata.dat")
z= data[:,0]
hzby1plusz= data[:,1]
sigmahzby1plusz=data[:,2]

Hz=[]
sigmaHz=[]

print(len(z))

for i in range(len(z)):
   Hz1 = (1+z[i])*hzby1plusz[i]
   sigma_Hz1 = Hz1 * (sigmahzby1plusz[i] / hzby1plusz[i])
   Hz.extend([Hz1])
   sigmaHz.extend([sigma_Hz1])

ac=np.c_[z,Hz]
ad=np.c_[ac,sigmaHz]
np.savetxt('z_Hz.txt',ad,delimiter=' ', fmt='%f')


