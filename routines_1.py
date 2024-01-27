import numpy as np
import scipy.integrate as integrate
from constants import *
from math import *
import xdata as xd
import numpy as np


def Fd(x): # disc flux
    f_d = cc*(1-np.sqrt(0/x))/x**3
    return( f_d )

def LT(t): # coronal X ray luminosity as a gaussian variation
    tau = 0.75*(24*3600)
    sd = 0.1*(24*3600)
    l = 2e37*np.exp(-0.5*(t - tau)**2/sd**2)
    return(l)

def d(x,a,phi): # distance of between 2 points one on the corona other on the disc ( a , phi ) are coronal polar coordinates. 
    dd = Rg*np.sqrt(x*x + hx*hx + a*a + 2*x*a* sin(phi)) + hx*Rg
    return(dd)

def d1(x): # distance of small corona
    dd = Rg*np.sqrt(x*x + hx*hx) + hx*Rg
    return(dd)     

def Bl(x,l,T): 
    if (h*c/(kb*T*l)) < 709:
        bb = (2*h*c**2/l**5)/(np.exp((h*c)/(kb*T*l))-1)
    elif (h*c/(kb*T*l)) >= 709:
        bb = (2*h*c**2/l**5)*np.exp(-(h*c)/(kb*T*l))   
    return( 0.25*bb )
    
def Bv(x,v,T): 
    if (h*v/(kb*T)) < 709:
        bb = (2*h*v**3/c**2)*(1/(np.exp((h*v)/(kb*T))-1))
    elif (h*v/(kb*T)) >= 709:
        bb = (2*h*v**3/c**2)*np.exp(-(h*v)/(kb*T))   
    return( bb )


def F1(frac,x,t): # xray flux for small corona
    dd = d1(x)
    f = frac*Rg*hx*xd.Ldata(t - dd/c)/(4*pi*(dd-hx*Rg)**3)
    return(f)

def Fth(frac,x,t): # xray flux for small corona
    dd = d1(x)
    f = frac*Rg*hx*LT(t - dd/c)/(4*pi*(dd-hx*Rg)**3)
    return(f)