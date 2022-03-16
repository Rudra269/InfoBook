# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:41:45 2019

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
max=15
plt.xlim(-max-1, max+1)  
plt.ylim(-max-1, max+1)

nP=100  # nombre de points choisis aléatoirement 

matP=alea.rand(2,nP)*2*max -max
visu_point(matP,'c.')

# rotation aléatoire d'un objet posé à l'origine :
##################################################################

matP_objet_init = np.array([[-5, -1, 0, 1, 5],
                            [ 0,  0, 2, 0, 0]])
P_origine = np.array([[0],
                      [0]])
vecN_init = np.array([[0], 
                      [3]])
    
#visu_point(matP_objet_init,'g-')
#visu_segment(P_origine, P_origine + vecN_init, 'g-')

theta_alea = alea.rand()*2*np.pi

matP_objet = np.dot(mat_rotation(theta_alea),matP_objet_init)

vecN = np.dot(mat_rotation(theta_alea),vecN_init)


#visu_point(matP_objet,'k-')
#visu_segment(P_origine, P_origine + vecN, 'k-')


# vision réduite d'un angle theta de chaque côté :
##################################################################

theta = 0  # choisir un autre angle si vision réduite



# tester la visibilité de chaque Point :
##################################################################
# affichage en rouge si visible

P_droite = P_origine  # le point sur " la droite "

for i in range(nP):
    vecteurP = np.array([[matP[0, i] - P_origine[0, 0]],
                         [matP[1, i] - P_origine[1, 0]]])
    prodScalaire = np.dot(vecteurP.T, vecN)
    if prodScalaire > 0 :
        visu_point(vecteurP,'g.')
    
    
    
    
    
#visu_point(matP_objet,'k-')
#visu_segment(P_origine, P_origine + vecN, 'k-')