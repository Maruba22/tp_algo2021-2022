# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 14:42:40 2023

@author: mrx
"""


from abc import abstractmethod, ABCMeta


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
    
class Rectangle(FGeometrique):
    """ Classe Rectangle avec juste son constructeur et quelques choses 
    pour demarrer"""
       
    def __init__(self,largeur, longueur):
       
        self.largeur = largeur if largeur >=0 else abs(largeur)
        self.longueur = longueur if longueur >=0 else abs(longueur)
              


class Cercle(FGeometrique):
    """ Classe Cercle avec juste son constructeur et quelques choses 
    pour demarrer"""
    
    def __init__(self, rayon):
        self.rayon = rayon if rayon >=0 else abs(rayon)
        
   
        
class Triangle(FGeometrique):
    """ Classe Triangle avec juste son constructeur et quelques choses 
    pour demarrer"""
    def __init__(self,longueur_a,longueur_b,longueur_c):
        self.longueur_a = longueur_a 
        self.longueur_b = longueur_b 
        self.longueur_c = longueur_c  
        
       
   
        