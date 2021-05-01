#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 14:27:38 2021

@author: maximelucas
"""

import numpy as np
import matplotlib.pyplot as plt

rho_max=250
v_max=130
long=1000
A=150
B=40000
ga=[0 for i in range(B)]
gb=[0 for i in range(B)]
rho0=[200 for i in range(A//5)]+[0 for i in range(4*A//5)]
deltaX = long/A
deltaT=deltaX * (1/(v_max+1))
rho_critique = 125

def gG(s1, s2):
    if (s1 <= 125 and s2 <= 125):
        res = f(s1)
    elif (s1 >= 125 and s2 >= 125):
        res = f(s2)
    elif (s1 < 125 and s2 > 125):
        res = min(f(s1),f(s2))
    else :
        res = f(125)
    return res
    #return f(s1)

def f(rho):
    res = rho*v(rho)
    return res
    
#def v(rho):
    #res = v_max
    #res = (v_max/rho_max)*(rho_max-rho)        
#    return res
    
def v(rho):
    res = v_max
    if rho != 0:
        res = np.sqrt(100*((1000/rho)-4)) 
    if res > v_max :
        res = v_max
    return res

def rho_c(X):
    l = (deltaT)/(deltaX)
    Y = [0 for i in range(len(X))]
    for i in range(1, len(X)-1):
        Y[i] = X[i] -( l * (gG(X[i], X[i+1]) - gG(X[i-1], X[i])))
    return Y


v = [v(i) for i in range(250)]
plt.plot(v)

#line, = plt.plot(rho0)
#X=rho0

#for i in range(1000):
#    X = rho_c(X)
#    line.set_ydata(X)
#    plt.pause(1e-4)
#    plt.draw()
