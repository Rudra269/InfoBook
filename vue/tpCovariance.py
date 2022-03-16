# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:21:26 2021

@author: ricord
"""

import numpy as np  
import matplotlib.pyplot as plt
import scipy.stats as stats


# exercice-1 : Calcul de la covariance et du coefficient de corrélation :
#########################################################################

def esperance(valX, proba):
    return sum(valX*proba)

def variance(valX, proba):
    esp = esperance(valX, proba)
    esp2 = esperance(valX*valX, proba)
    var = esp2 - esp*esp
    return var
    
def covariance (valX, valY, proba):
    valXY = valX*valY
    esp = esperance(valXY, proba)
    esp2 = esperance(valY, proba)
    esp3 = esperance(valX, proba)
    cov = esp - esp2*esp3
    return cov

def coefCorr (valX, valY, proba):
    valXY = valX*valY
    esp = esperance(valXY, proba)
    esp2 = esperance(valY, proba)
    esp3 = esperance(valX, proba)
    cov = esp - esp2*esp3
    coef = cov/np.sqrt(variance(valX, proba))*np.sqrt(variance(valY, proba))
    return coef

valeur_X_seul = [-1, 0, 1]
valeur_Y_seul = [0, 1]

lenX = len(valeur_X_seul)
lenY = len(valeur_Y_seul)

taille = lenX*lenY

# des tableaux de même taille :

proba_couple = np.array([[0, 1/3, 0, 1/3, 0, 1/3]]).reshape(taille,1)

valeur_X = np.array([valeur_X_seul]*len(valeur_Y_seul)).reshape(taille,1)

valeur_Y = np.dot(np.diag(valeur_Y_seul),np.ones((lenY,lenX))).reshape(taille,1)

#valeur_Y = np.array([[0, 0, 0, 1, 1, 1]]).reshape(taille,1)

valeur_XY = valeur_X*valeur_Y
print(valeur_XY)

# calcul des paramètres :

esp_X = esperance(valeur_X,proba_couple)
var_X = variance(valeur_X,proba_couple)

esp_Y = esperance(valeur_Y,proba_couple)
var_Y = variance(valeur_Y,proba_couple)

esp_XY = esperance(valeur_XY,proba_couple)
cov = covariance(valeur_X, valeur_Y, proba_couple)
print(cov)
corr = coefCorr(valeur_X, valeur_Y, proba_couple)
print(corr)

print(esp_X, esp_Y, esp_XY, cov, corr)


# exercice-2 : Simuler N observations d'une loi Normale :
#########################################################################
N = 100
echantillon = []

for k in range(N):
    n = 200
    U = np.random.rand(n)
    
    # normailiser ces valeurs afin de pouvoir utiliser le théorème (TLC) :
#    Y = TODO
    
#    new_valeur = TODO
    
#    echantillon.append(new_valeur)

# visualiser l'histogramme des valeurs simulées :
plt.hist(echantillon, bins=30, alpha=0.7)
#plt.hist(echantillon, bins=30, density=True, color='g', edgecolor='red', alpha=0.7)


# exercice-3 : Table de la loi LNCR :
#########################################################################
# The main public methods for continuous RVs are:\\
# cdf: Cumulative Distribution Function\\
# ppf: Percent Point Function (Inverse of CDF)\\
    
# Pour la loi Normale, retrouver des valeurs que vous pouvez lire sur la table,
# en utilisant ces functions :
# stats.norm.cdf()
# stats.norm.ppf() -> permet de calculer les quantiles, la médiane par ex.

# On cherche d tel que : P( m - d < X < m + d) = 1 - alpha
# lorsque X suit une loi Normale(m,sigma)
# Ecrire une fonction qui renvoie la valeur d 
# et ayant pour paramètres alpha, m et sigma

#def ecart_autour_moy(alpha,m,sigma):