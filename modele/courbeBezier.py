# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:32:27 2019

@author: ricord
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:40:25 2019

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

def visu_BezierQuad(matPointControl,str):
    
    n=50
    mt = np.linspace(0,1.,n)  
    matt = np.ones((3,n))  # que des 1
    matt[1,:] = mt  # ligne avec les t
    matt[2,:] = mt*mt  # ligne avec les t*t
    
    matBezier3 = np.array([[1, 0, 0], 
                           [-2, 2, 0], 
                           [1, -2, 1]])

    matPointligne = np.dot(np.dot(matt.T,matBezier3),matPointControl.T)
    matPoint=matPointligne.T  # on transpose

    visu_point(matPointControl,'k-')
    #visu_point(matPointControl,'k.')
    #visu_point(matPoint,str)
    
def visu_BezierCubic(matPointControl,str):
    
    n=50
    
    mt = np.linspace(0,1.,n)  
    matt = np.ones((4,n))  # que des 1
    matt[1,:] = mt  # ligne avec les t
    matt[2,:] = mt*mt
    matt[3,:] = mt*mt*mt# ligne avec les t*t

    matBezier4 = np.array([[1, 0, 0, 0], 
                           [-3, 3, 0, 0], 
                           [3, -6, 3, 0], 
                           [-1, 1, -1, 1]])
    
    
    matPointligne = np.dot(np.dot(matt.T,matBezier4),matPointControl.T)
    matPoint=matPointligne.T  # on transpose

#    visu_point(matPointControl,'k-')
#    visu_point(matPointControl,'g:')
    visu_point(matPoint,str)


# *********************************************************

plt.axis('scaled') # la position est importante
xmin, xmax = plt.xlim(-20, 20)  # pour délimiter la fenêtre
ymin, ymax = plt.ylim(-20, 20)

p1 = np.array([[0, 0, 5, 0], 
               [18, 5, -5, 18]])

#visu_BezierCubic(p1, 'r-')

for angle in np.linspace(0, 2*np.pi, 5):
    p = np.dot(mat_rotation(angle), p1)
    visu_BezierCubic(p, 'r-')
#p2 = np.dot(mat_rotation(np.pi/2), p1)
#p3 = np.dot(mat_rotation(np.pi), p1)
#p4 = np.dot(mat_rotation(-(np.pi)/2), p1)
#
#p5 = np.dot(mat_rotation(np.pi/4), p1)
#p6 = np.dot(mat_rotation(3(np.pi)/4), p1)
#p7 = np.dot(mat_rotation(-(np.pi)/2), p1)

#visu_BezierQuad(p1, 'r-')
#visu_BezierQuad(p2, 'r-')
#visu_BezierQuad(p3, 'r-')
#visu_BezierQuad(p4, 'r-')


#visu_segment(Pi1, Pi2, ':')

# courbe de Bezier quadratique : un exemple  ***************

#matPointControl = TODO
#
#
## effectuer une rotation de cette courbe : *********************
#
#TODO
#    
#
## courbe de Bezier cubique : un exemple  ***************
#
#TODO
#
#
## recoller deux courbes de Bezier cubiques ( 4 points de controle ) :
#
#TODO

