# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 13:08:02 2021

@author: rroy
"""
import numpy as np  
import matplotlib.pyplot as plt


def trace_cercle(a, b, r):
    t = np.linspace(0, np.pi*2,30)
    x = a + np.cos(t)*r
    y = b + np.sin(t)*r
    plt.plot(x,y,'r:')
   
    
def trace_droite(pente, b):
    x = np.linspace(xmin, xmax,30)
    y = pente*x + b
    plt.plot(x,y,'b:')
 
    
def matP_homogene(matP):  
    # la matrice des points écrits en coordonnées homogènes
    nP=matP.shape[1] 
    matP_h = np.concatenate((matP,np.ones((1,nP))),0)
    return matP_h


def affiche_polygone(matP, string):
## en ajoutant le point final    
#    pointdebut=matP[:,0]
#    pointdebut=pointdebut.reshape(pointdebut.shape[0],1)
#    matP=np.concatenate((matP,pointdebut),1)
#    # on peut faire directement cela :
    x = matP[0, :]
    y = matP[1, :]
    plt.plot(x, y, string)


def mat_Rotation_h(theta):
    mat = np.array([[np.cos(theta), -np.sin(theta), 0],
                    [np.sin(theta), np.cos(theta), 0],
                    [0, 0, 1]])
    return mat


def mat_Translation_h(tx,ty):
    mat = np.array([[1, 0, tx],
                    [0, 1, ty],
                    [0, 0, 1]])
    return mat


def mat_Reflexion_axe1():
    mat = np.array([[1, 0, 0],
                    [0, -1, 0],
                    [0, 0, 1]])
    return mat


def mat_Scale_h(sx,sy):
    mat = np.array([[sx, 0, 0],
                    [0, sy, 0],
                    [0, 0, 1]])
    return mat



plt.axis('scaled') # la position est importante
xmin, xmax = plt.xlim(-10, 30)  # pour délimiter la fenêtre
ymin, ymax = plt.ylim(-10, 25)

r=6
trace_cercle(0, 0, r)
plt.plot([0], [0], 'ro')


# matrice des points de l'objet de référence :
matP=np.array([[0, 2, 0, 1, 0, 0],
                [0, 0, 2, 2, 4, 0]])
matP=matP_homogene(matP)


matP1 = np.dot(mat_Translation_h(r,0), matP)
#affiche_polygone(matP1, 'b:')

tab_angle = np.linspace(0, np.pi*2, 10) # un array
for theta in tab_angle:
    matP2 = np.dot(mat_Rotation_h(theta), matP1)
    affiche_polygone(matP2, 'r-')

    
# une matrice de points choisis aléatoirement 
# chaque coordonnée suit une loi uniforme sur l'intervalle [0,1]    
matP_alea=np.random.rand(2,20)
#P_origine=np.array([[0], [0]])  # on peut ajouter l'origine à ces points
#matP_alea=np.concatenate((matP_alea,P_origine),1)
matP_alea=matP_homogene(matP_alea)
#affiche_polygone(matP_alea, 'k-')


# Agrandir une première fois :
matP_alea_1= np.dot(mat_Scale_h(5, 5), matP_alea)
#affiche_polygone(matP_alea_1, 'y-')


# Agrandir encore, Tourner (angle theta), Déplacer (droite y=p.x) :

matP_alea_2= np.dot(mat_Scale_h(5, 5), matP_alea_1)

theta=np.pi*0.2
pente = np.tan(theta)
trace_droite(pente, 0.)
matP_alea_3= np.dot(mat_Rotation_h(pente), matP_alea_2)
affiche_polygone(matP_alea_3, 'g-')

x=12
matP_alea_4= np.dot(mat_Reflexion_axe1(), matP_alea_3)
#affiche_polygone(matP_alea_4, 'b-')

matP_alea_5 = np.dot(mat_Translation_h(0, pente*x), matP_alea_4)
affiche_polygone(matP_alea_5, 'k-')

# Relexion par rapport à la droite y=px :

"""TODO
TODO
TODO"""

#plt.show()