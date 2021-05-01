#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:05:13 2021

@author: maximelucas
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio
import os
from mpl_toolkits.mplot3d import Axes3D

rho_max=250.0
v_max=130.0
T = 3
long=200
A=50
B=100
ga=[0 for i in range(B)]
gb=[0 for i in range(B)]
rho0=[0 for i in range(A//5)]+[200 for i in range(A//5)]+[0 for i in range(A//5)]+[200 for i in range(A//5)]+[0 for i in range(A//5)]
    
# delta T = moins de 1 X (1/max(f' sur ab) x delta x)

def init_matrice(A, B, ga, gb, rho0):
    G = np.zeros((A,B))
    G[0,:]=ga
    G[A-1,:]=gb
    G[:,0]=rho0
    
    return G

def gG(s1, s2):
    if (s1 <= rho_max/2 and s2 <= rho_max/2):
        res = f(s1)
    elif (s1 >= rho_max/2 and s2 >= rho_max/2):
        res = f(s2)
    elif (s1 < rho_max/2 and s2 > rho_max/2):
        res = min(f(s1),f(s2))
    else :
        res = f(rho_max/2)
    return res

def f(rho):
    res = rho*v(rho)
    return res
    
#def v(rho):
#    res = (v_max/rho_max)*(rho_max-rho)        
#    return res

def v(rho):
    res = v_max
    if rho != 0:
        res = np.sqrt(100*((1000/rho)-4)) 
    if res > v_max :
        res = v_max
    return res
    

def rho_c(G,j,n):
    l = (T*A)/(long*B)
    res = G[j, n-1] -( l * (gG(G[j, n-1], G[j+1, n-1]) - gG(G[j-1, n-1], G[j, n-1])))
    return res

def remplissage(A,B,ga,gb,rho0):
    G=init_matrice(A, B, ga, gb, rho0)
    for n in range(1,B):
        for j in range(1,A-1):
            G[j, n] = rho_c(G,j,n)
    return G

def affichage(G):
    X=[]
    Y=[]
    Z=[]
    for n in range(0,B):
        for j in range(0,A):
            X.append(n)
            Y.append(j)
            Z.append(G[j,n])
    fig = plt.figure()
    ax=fig.gca(projection='3d')
    ax.scatter(X,Y,Z,zdir="z", s=40, depthshade=True)
    plt.show()




G=remplissage(A, B, ga, gb, rho0)
x = np.linspace(0, long, A)

fig = plt.figure() # initialise la figure
line, = plt.plot([],[]) 
plt.xlim(0, long)
plt.ylim(0,250)

# fonction à définir quand blit=Trues
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line.set_data([],[])
    return line,

def animate(i): 
    line.set_data(x, G[:,i])
    return line,
 
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, blit=True, interval=300, repeat=False)

plt.show()



#G=remplissage(A, B, ga, gb, rho0)
#affichage(G)


#### GIF ####
def creer_gif():
    H=remplissage(A, B, ga, gb, rho0)
    x = np.linspace(0, long, A)
    filenames=[]
    for i in range(B):
        plt.figure(i+20)
        plt.plot(x, G[:,i])
        plt.ylim(0,5)
        filenames.append(str(i)+'.png')
        plt.savefig(filenames[-1])
        plt.show()
    with imageio.get_writer('mygif.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
    for filename in set(filenames):
        os.remove(filename)


