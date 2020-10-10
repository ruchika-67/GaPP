import numpy as np
data = np.loadtxt("z_Hz.txt")

z= data[:,0]
Hz=data[:,1]
Hz_sigma = data[:,2]

H0= 53.6736436423  
H0_sigma = 5.47649377858

Ez=[]
sigma_Ez= []
print(len(z))

for i in range(len(z)):
   Ez_1 = (Hz[i]/H0)
   sigma_Ez1 = np.sqrt((Hz_sigma[i]/H0)**2.+((Hz[i]/H0**2.)*H0_sigma)**2.)
   Ez.extend([Ez_1])
   sigma_Ez.extend([sigma_Ez1])

ac=np.c_[z,Ez]
ad=np.c_[ac,sigma_Ez]
np.savetxt('z_Ez.txt',ad,delimiter=' ', fmt='%f')
