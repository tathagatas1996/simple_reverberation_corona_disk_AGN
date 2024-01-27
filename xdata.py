import scipy.integrate as integrate
import scipy.interpolate as interp
import numpy as np
from constants import *
from routines_1 import *

# Corona light-curve
time = np.loadtxt('xray_lc1',usecols = (0,))
time = (time - min(time))*3600*24 # convert to seconds
xray = np.loadtxt('xray_lc1',usecols = (2,))

xray1 = np.zeros((len(xray) + 2),dtype = np.float128)
time1 = np.zeros((len(xray) + 2),dtype = np.float128)
La = min(xray)

tM = (Rg/c)*np.sqrt(x_out*x_out + hx*hx) + hx*Rg/c 
tm = (Rg/c)*np.sqrt(x_in*x_in + hx*hx) + hx*Rg/c


for i in range(len(xray1)):
    if i == 0:
        xray1[i] = La
        time1[i] = time[0] - tM - 1
    elif i == len(xray1) - 1 :
        xray1[i] = La
        time1[i] = time[i-2] + tm
    else :
        xray1[i] = xray[i-1]
        time1[i] = time[i-1]
        
def Ldata(t):
    i0 = 0
    global xray1
    global time1
    index = np.where(t>time1)
    index = index[0]
    nn = len(index)
    i0 = index[nn-1]
    m0 = (xray1[i0+1] - xray1[i0]) / (time1[i0+1] - time1[i0])
    c0 = xray1[i0] - m0*time1[i0]
    ll = m0*t + c0
    return(ll)
