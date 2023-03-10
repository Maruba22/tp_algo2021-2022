# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 23:02:08 2023
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
        
    
    
class Rectangle(FGeometrique):
       
    def __init__(self,largeur, longueur):
        self.largeur = largeur if largeur >=0 else abs(largeur)
        self.longueur = longueur if longueur >=0 else abs(longueur)       
        FGeometrique.nb_rectangle = self.nb_rectangle + 1 
        
    
    def getSurface(self):
        return self.largeur * self.longueur
        
            
    def getPerimetre(self):
        return 2*(self.longueur + self.largeur)
    
    def monRectangle(self):
        
        print(f" \n --Rectangle {self.nb_rectangle}--   \n\n Longueur : {self.longueur} [m] \n Largeur : {self.largeur} [m]")
        print(f" Couleur : {self.couleur} \n Surface : {self.getSurface()} [m²] \n Perimetre : {self.getPerimetre()} [m] ")
        
    def dessiner(self):               
        for i in range(1, self.longueur+1):
            for j in range(1, self.largeur+1):
                if i==1 or i==self.longueur or j==1 or j==self.largeur:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
        
class Cercle(FGeometrique): 
    def __init__(self, rayon):
        self.rayon = rayon if rayon >=0 else abs(rayon)
        FGeometrique.nb_cercle = self.nb_cercle +1    
    def getPerimetre(self):
        return round(2*pi*self.rayon,3)
    
    def getSurface(self):        
        return round(pi*(self.rayon**2),3)
    
    def monCercle(self):
        print(f" \n ** Cercle {self.nb_cercle} **   \n\n Rayon : {self.rayon} [m] \n Perimetre : {self.getPerimetre()} [m] \n Surface : {self.getSurface()} [m²] ")
        print(f" Couleur : {self.couleur} \n ")
        
        
class Triangle(FGeometrique):
    
    def __init__(self,longueur_a,longueur_b,longueur_c):
        self.longueur_a = longueur_a if longueur_a >=0 else abs(longueur_a)
        self.longueur_b = longueur_b if longueur_b >=0 else abs(longueur_b)
        self.longueur_c = longueur_c if longueur_c >=0 else abs(longueur_c)     
        
        FGeometrique.nb_triangle = self.nb_triangle + 1
       
   
    def getSurface(self):
        x = (self.longueur_a+self.longueur_b+self.longueur_c)/2
        sur = sqrt(abs(x*(x-self.longueur_a)*(x-self.longueur_b)*(x-self.longueur_c)))

        return round(sur,3)
    
    def getPerimetre(self):
        return self.longueur_a + self.longueur_b + self.longueur_c
    
    def monTriangle(self):
        print(f" \n ++  Triangle {self.nb_triangle} ++   \n\n Cote_1 : {self.longueur_a} [m] \n Cote_2 : {self.longueur_b} [m] \n Cote_3 : {self.longueur_c} [m] \n Perimetre : {self.getPerimetre()} [m] \n Surface : {self.getSurface()} [m²] ")
