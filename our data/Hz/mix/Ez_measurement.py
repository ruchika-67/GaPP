# ======== important packages to be imported 
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
import sys as sys

from gapp import gp, dgp, covariance
import pickle
import numpy as np
from numpy import array,concatenate,loadtxt,savetxt,zeros
import matplotlib.pyplot as plt
from matplotlib import rc
 
if __name__=="__main__":

    #======== loading cosmological data
    filename = 'z_EzH0'
    (Zh0,Hzh0,Sigmah0) = loadtxt(filename+'.txt',unpack='True')

    #======== Gaussian process: reconstructing H(z) from data, starting from zmin = 0 all the way to zmax from data 
    zmin = 0.
    zmax = np.max(Zh0)
    g1 = gp.GaussianProcess(Zh0,Hzh0,Sigmah0,covfunction=covariance.SquaredExponential,cXstar=(zmin,zmax,200))

    (rec1h0,theta1h0) = g1.gp(thetatrain='True')


    #===== creating variables to receive the GP reconstructed Hz 
    zrech0 = rec1h0[:,0]
    hzrech0 = rec1h0[:,1]
    sighzrech0 = rec1h0[:,2]
    
    # ======= printing the reconstructed H(z) at the lowest point, i.e., zmin=0, and its relative uncertainty 
    print 'z=', zrech0[0], ' H0=', hzrech0[0], ' sigH0=',  sighzrech0[0], ' sigH0/H0 (%)=', (sighzrech0[0]/hzrech0[0])*100.
        
    # ========== saving the reconstructed hz and its derivatives
    savetxt("ez_rech0.dat",rec1h0)

    #======== loading cosmological data
    filename = 'z_Ez'
    (Z,Hz,Sigma) = loadtxt(filename+'.txt',unpack='True')

    #======== Gaussian process: reconstructing H(z) from data, starting from zmin = 0 all the way to zmax from data 
    zmin = 0.
    zmax = np.max(Z)
    g1 = gp.GaussianProcess(Z,Hz,Sigma,covfunction=covariance.SquaredExponential,cXstar=(zmin,zmax,200))
    (rec1,theta1) = g1.gp(thetatrain='True')

    #===== creating variables to receive the GP reconstructed Hz 
    zrec = rec1[:,0]
    hzrec = rec1[:,1]
    sighzrec = rec1[:,2]
    
    # ======= printing the reconstructed H(z) at the lowest point, i.e., zmin=0, and its relative uncertainty 
    print 'z=', zrec[0], ' H0=', hzrec[0], ' sigH0=',  sighzrec[0], ' sigH0/H0 (%)=', (sighzrec[0]/hzrec[0])*100.
        
    # ========== saving the reconstructed hz and its derivatives
    savetxt("ez_rec.dat",rec1)


##############################################################################
    #======== loading cosmological data


    filename1 = 'Hdata'
    filename2 = 'Hsigma'
    (Zpanth,Hzpanth) = loadtxt(filename1+'.dat',unpack='True')
    (Sigmapanth) = loadtxt(filename2+'.dat',unpack='True')

    #======== Gaussian process: reconstructing H(z) from data, starting from zmin = 0 all the way to zmax from data 
    zmin = 0.
    zmax = np.max(Zpanth)
    g1 = gp.GaussianProcess(Zpanth,Hzpanth,Sigmapanth,covfunction=covariance.SquaredExponential,cXstar=(zmin,zmax,200))
    (rec1panth,theta1panth) = g1.gp(thetatrain='True')

    #===== creating variables to receive the GP reconstructed Hz 
    zrecpanth = rec1panth[:,0]
    hzrecpanth = rec1panth[:,1]
    sighzrecpanth = rec1panth[:,2]
    
    # ======= printing the reconstructed H(z) at the lowest point, i.e., zmin=0, and its relative uncertainty 
    print 'z=', zrecpanth[0], ' H0=', hzrecpanth[0], ' sigH0=',  sighzrecpanth[0], ' sigH0/H0 (%)=', (sighzrecpanth[0]/hzrecpanth[0])*100.
        
    # ========== saving the reconstructed hz and its derivatives
    savetxt("ez_recpanth.dat",rec1)


    
    # ========== Plotting the real data points and reconstructed H(z) curves - from 1 to 3sigma
#    plt.errorbar(Zh0, Hzh0, yerr=Sigmah0, fmt='o', color='black')
#    ax.fill_between(zrech0, hzrech0+1.*sighzrech0, hzrech0-1.*sighzrech0, facecolor='violet', alpha=0.80, interpolate=True)

###################################################################################3
########################################################################################
########################################################################################
#########################################################################################
############################################################################################



    # ====== Create figure size in inches
    fig, ax = plt.subplots(figsize = (9., 7.))

    # ========= Define axes
    ax.set_xlabel(r"$z$", fontsize=22)
    ax.set_ylabel(r"$E(z)$", fontsize=22)
    plt.xlim(zmin, 2.0)
    for t in ax.get_xticklabels(): t.set_fontsize(22)
    for t in ax.get_yticklabels(): t.set_fontsize(22)    
    # ========== Plotting the real data points and reconstructed H(z) curves - from 1 to 3sigma
#    plt.errorbar(Z, Hz, yerr=Sigma, fmt='o', color='black')
    ax.fill_between(zrec, hzrec+1.*sighzrec, hzrec-1.*sighzrec, facecolor='#F08080', alpha=0.80, interpolate=True)
    ax.fill_between(zrech0, hzrech0+1.*sighzrech0, hzrech0-1.*sighzrech0, facecolor='violet', alpha=0.80, interpolate=True)
    ax.fill_between(zrecpanth, hzrecpanth+1.*sighzrecpanth, hzrecpanth-1.*sighzrecpanth, facecolor='blue', alpha=0.80, interpolate=True)
    plt.legend((r"$E(z)$ rec (without H0)", "$E(z)$ rec (with H0)"), fontsize='22', loc='upper left')
#    plt.show()
    # =========== saving the plot
    plt.savefig('Ez1.pdf', bbox_inches='tight')
#    fig.savefig(filename+'_reconst.pdf')
#    plt.savefig('sc.pdf', bbox_inches='tight')


    
