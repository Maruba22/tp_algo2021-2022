# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 14:37:34 2023

@author: mrx

"""

  
from math import pi
from abc import abstractmethod, ABCMeta
from math import sqrt

class FGeometrique:
    
    couleur = "White"   
    nb_rectangle = 0 
    nb_cercle = 0
    nb_triangle = 0    
    
    def __init__(self,couleur,surface,perimetre):
        self.couleur = couleur 
        self.surface = surface
        self.perimetre = perimetre      
        
    @abstractmethod 
    def getCouleur(self):
        return self.couleur
    
    @abstractmethod 
    def setCouleur(self,couleur):
        self.couleur = couleur
        return self.couleur
    
    @abstractmethod 
    def getSurface(self,surface):       
       return self.surface
   
    @abstractmethod
    def getPerimetre(self,perimetre):
        return self.perimetre