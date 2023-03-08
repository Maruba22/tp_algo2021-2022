"""
Created on Tue Jan  3 06:17:52 2023

@author:mrx
"""
from reponse_4 import *

class DataRectangle:
    def __init__(self):
        self.l = float(input("longueur ..."))
        self.L = float(input("Largeur ..."))        
        
    def surfaceRectangle(self):        
        rec = Rectangle(self.L, self.l)
        return print(rec.getSurface())
    
    def perimetreRectangle(self):        
        rec = Rectangle(self.L, self.l)
        return print(rec.getPerimetre())
    
    
d = DataRectangle()
d.surfaceRectangle()
d.perimetreRectangle()
