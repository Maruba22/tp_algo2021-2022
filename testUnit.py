import reponse_7 as moncode
import unittest 


"""J'importe le fichier dans lequel se trouve nos classes
Rectangle,  Carre, Triangle,...
Et aussi J'importe le module pour tester mes classes
 """
 
rect = moncode.Rectangle(1,1)
cerc = moncode.Cercle(2)
tria = moncode.Triangle(4, 4, 6)

class TestModule(unittest.TestCase):
    
    def test_triangle(self):
        self.assertEqual(rect.getSurface(),1)
        self.assertEqual(rect.getCouleur(),'Blue')
        self.assertEqual(rect.getPerimetre(),4)
        
        
    
    def test_carre(self):        
        self.assertTrue(cerc.getSurface(),12.566)
        self.assertTrue(cerc.getCouleur(),'Blue')
        self.assertTrue(cerc.getPerimetre(),4)
        
    def test_tria(self):
        self.assertEqual(tria.getSurface(),1)
        self.assertEqual(tria.getCouleur(),'Blue')
        self.assertEqual(tria.getPerimetre(),4)
        
        
if __name__=='__main__':
    unittest.main()
