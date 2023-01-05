# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 06:17:52 2023

@author:mrx
"""

from math import pi
from abc import abstractmethod, ABCMeta
from math import sqrt

class FGeometrique:
    noms_developpeurs = "Maruba Exaucé , Twite , Murhabazi"
    couleur = "Blue"   
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


        
    @classmethod 
    def Carre(cls,cote):
        return cls(cote,cote)
    
        
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
        print(f" Couleur : {self.couleur} \n ")
      
    @classmethod    
    def Rectangle(cls,a,b):
        return cls(a,b,sqrt((a**2 +b**2)))




class DataRectangle:
    def __init__(self):
        self.l = float(input("Entrer la longueur :"))
        self.L = float(input("Entrer la Largeur :"))        
        
    def surfaceRectangle(self):        
        rec = Rectangle(self.L, self.l)
        return print(rec.getSurface())
    
    def perimetreRectangle(self):        
        rec = Rectangle(self.L, self.l)
        return print(rec.getPerimetre())
    
if __name__ == '__main__':
    print("\n Ma batterie de test complete...")
    
    print("Test rectangle")
    r = Rectangle(12,5)
    print(r)
    print("Largeur :  ",r.largeur,"Longueur : " , r.longueur, "Couleur ", r.couleur)
    r.setCouleur("Grise")
    print("Nouvelle couleur  : ", r.couleur)
    
    print("Surface : ", r.getSurface(), "Perimetre : ", r.getPerimetre(), "\n")
    r.dessiner()
    r.monRectangle()
    
    
    r_2 = Rectangle(3,8)
    r_2.setCouleur("Orange")
    r_2.monRectangle()
    r_2.dessiner()
    
    print("test carré")
    car  = Rectangle.Carre(12)
    car.setCouleur("Violet")
    car.monRectangle()
    car.dessiner()
    print(car.longueur)
    
    print("test triangle")
    tr = Triangle(5,8,9)
    print("Mes cotés sont : ",tr.longueur_a, tr.longueur_b, tr.longueur_c)
    
    tr.monTriangle()

    tr.setCouleur("Blanc")
    print(tr.getPerimetre())
    print(tr.getSurface())
    print(tr.getCouleur())
    
    print("test cercle")
    cer = Cercle(16)
    cer.monCercle()
    cer.setCouleur("Noir")
    cer.rayon = 50
    cer.monCercle()
    
    
    trian = Triangle(4,9,10)
    trian.setCouleur("Verte")
    trian.monTriangle()
    
    trianCed = Triangle(12,12,12)
    trianCed.setCouleur("Rouge")
    trianCed.monTriangle()




    
    
    
    
