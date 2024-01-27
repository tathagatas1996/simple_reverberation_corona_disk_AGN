#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 19:40:18 2017
python def_routines.py build_ext --inplace
@author: tathagata
"""

from math import *
import numpy as np
import scipy.constants as cons

c = cons.c # speed of light
G = cons.G # gravitational constant
kb = cons.k # Boltzman constant
s = cons.Stefan_Boltzmann # stephan boltzman constant
h = cons.h
M0 = np.float(1.998E30) # Mass of sun
L0 = np.float(3.8468E26) # Luminosity of sun
# Parameters
hx = np.float(2.5) # perpendicular ht. of the corona above the disc
M =  (1.8e8)*M0#(10**8.92)*M0
L_edd = np.float(3.2*10**4*(M/M0) *L0)
Rg =np.float( 2*G*M/c**2)
tsc = Rg/c # time scale for the system
x_in = np.float(1)
x_out= np.float(1000)
epsilon = 0.05
eta = 0.1
rc = 1.5
#sigma_T = 
M_dot = np.float( epsilon*L_edd/(eta*c**2))
cc = np.float( 3*G*M*M_dot/(8*np.pi*Rg**3)) ## Shakura Sunyaev disk flux