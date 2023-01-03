# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 14:37:34 2023

@author: mrx

Nous créons justa la classe FGeometrique sans l'implenter dans un premier temps
"""



class FGeometrique:
    
    """ La classe de base ou superclasse Forme géometrique"""    
    
    def __init__(self,couleur,perimetre,surface):
        self.couleur = couleur
        self.perimetre = perimetre      
        self.surface = surface
        
        
   
        