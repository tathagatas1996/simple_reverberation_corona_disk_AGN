from multiprocessing import Pool
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import timeit
from constants import *
from routines_1 import *
from math import *


def bb1(x,v,t): # Evaluate black body at a given frequency and radius
    T = np.power(((Fd(x) + Fth(1,x,t))/s),0.25)
    bb = Bv(x,v,T)
    return(bb)

def fp(t):
    SS = 0
    xo_temp = 0
    for i in range(3,100,5):    
        xi = i
        xo = i + 5
        ff0 = integrate.quad(lambda x : x*bb1(x,v,t) , xi , xo)
        SS = SS + ff0[0]
        xo_temp = xo
    for i in range(xo_temp, np.int(x_out)-5,5):
        xi = i
        xo = i + 5
        ff0 = integrate.quad(lambda x : x*bb1(x,v,t) , xi , xo)
        SS = SS + ff0[0]  
    return(SS)
    

if __name__ == "__main__":
    l_nm = 100
    i = np.int((l_nm - 100)/50 + 1) # just a label
    print(i)
    l = l_nm*1e-9
    v = c/l
    dL = 6.758e+24 #Distance in metres
    time0 = np.arange( 0 , 1212.3*tsc , 10*tsc , dtype = np.float64 ) #153238
    #------------------------------------------------
    start = timeit.default_timer()
    p1 = Pool()
    intensity0 = p1.map(fp , time0)
    intensity0 = np.array(intensity0)*2*np.pi*Rg**2/(dL**2*1e-29)
    stop = timeit.default_timer()
    time0 = time0/(3600*24)
    print((stop - start)/60)
    #------------------------------------------------
    #DataOut = np.column_stack((time0,intensity0))
    #np.savetxt("t10_new_hx100_new_r3by4_lx_func/"+str(i)+"lc"+str(l_nm),DataOut)