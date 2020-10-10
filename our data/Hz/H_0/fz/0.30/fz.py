import numpy as np
data = np.loadtxt("Hdata.dat")

z= data[:,0]
Hz=data[:,1]
Hz_sigma = data[:,2]

H0= 73.7936971284
H0_sigma = 1.37500450068

fz=[]
sigma_fz= []
om0= 0.3
print(len(z))

for i in range(len(z)):
   fz_1 = ((Hz[i]/H0)**2./(1.- om0)) - ((om0*(1.+z[i])**3.)/(1. - om0))
   sigma_fz1 = (2.* fz_1*np.sqrt((Hz_sigma[i]/H0)**2.+((Hz[i]/H0**2.)*H0_sigma)**2.))/ (Hz[i]/H0)
   fz.extend([fz_1])
   sigma_fz.extend([sigma_fz1])

ac=np.c_[z,fz]
ad=np.c_[ac,sigma_fz]
np.savetxt('z_fz.txt',ad,delimiter=' ', fmt='%f')
