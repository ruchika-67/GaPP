import numpy as np
data = np.loadtxt("Hdata.dat")

z= data[:,0]
Hz=data[:,1]
Hz_sigma = data[:,2]

H0= 74.03 #73.7936971284
H0_sigma = 1.42#1.37500450068

om=[]
sigma_om= []

print(len(z))

for i in range(len(z)):
   Ez_1 = (Hz[i]/H0)
   sigma_Ez1 = np.sqrt((Hz_sigma[i]/H0)**2.+((Hz[i]/H0**2.)*H0_sigma)**2.)
   om_1 = ((Hz[i]/H0)**2.-1.)/ ((1.+z[i])**3.-1.)
   sigma_om1 = (om_1*2.*sigma_Ez1)/Ez_1
   om.extend([om_1])
   sigma_om.extend([sigma_om1])

ac=np.c_[z,om]
ad=np.c_[ac,sigma_om]
np.savetxt('z_om.txt',ad,delimiter=' ', fmt='%f')
