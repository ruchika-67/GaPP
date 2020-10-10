import numpy as np
data = np.loadtxt("z_Ez.txt")

z= data[:,0]
Ez=data[:,1]
Ez_sigma = data[:,2]

#H0= 73.7936971284
#H0_sigma = 1.37500450068

om=[]
sigma_om= []

print(len(z))

for i in range(len(z)):
   Ez_1 = (Ez[i])
   sigma_Ez1 = Ez_sigma[i]
   om_1 = (Ez[i]**2.-1.)/ ((1.+z[i])**3.-1.)
   sigma_om1 = (om_1*2.*sigma_Ez1)/Ez_1
   om.extend([om_1])
   sigma_om.extend([sigma_om1])

ac=np.c_[z,om]
ad=np.c_[ac,sigma_om]
np.savetxt('z_om.txt',ad,delimiter=' ', fmt='%f')
