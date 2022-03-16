# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:32:28 2019

@author: ricord
"""

import numpy as np  
import matplotlib.pyplot as plt
import numpy.random as alea

def visu_point(matPoint,style):
    # matPoint contient les coordonnées des points 
    x = matPoint[0, :]
    y = matPoint[1, :]
    plt.plot(x, y, style)
    
def visu_segment(P1,P2,style):
    # attention P1 et P2 sont des tableaux (2,1)
    matP = np.concatenate((P1,P2),1)
    visu_point(matP,style)
    
def mat_rotation(theta):
    # si pas besoin des coordonnées homogènes
    mat = np.array([[np.cos(theta), -np.sin(theta)],
                    [np.sin(theta), np.cos(theta)]])
    return mat


plt.axis('scaled') # la position est importante
taille = 10
delta = 2
plt.xlim(-taille-delta, taille+delta)  
plt.ylim(-taille-delta, taille+delta)

# le segment (A,B) et son vecteur normal :

nP=2  # 2 points pour le segment
matP=alea.rand(2,nP)*2*taille - taille
visu_point(matP,'k-')

A = matP[:,0].reshape(2,1) #print(matP[:,0])  #print(A)
B = matP[:,1].reshape(2,1)
vecAB = B-A
vecN = np.dot(mat_rotation(np.pi/2),vecAB)

# le point source S et le vecteur du lancé de rayon :

S = np.array([[-5],
              [-5]])
vecS = alea.rand(2,1)
norme = np.sqrt(np.dot(vecS.T,vecS))
vecS = vecS*(1/norme)

# le point d'impact et sa visualisation :


# TODO





visu_point(S,'bo')
visu_segment(S,S+vecS*2,'b-')
visu_segment(S,S+vecS*7,'b:')
visu_point(A,'ko')
visu_point(B,'ko')