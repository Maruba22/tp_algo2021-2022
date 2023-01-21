import reponse_7 as moncode
import unittest 


"""J'importe le fichier dans lequel se trouve nos classes
Rectangle,  Carre, Triangle,...
Et aussi J'importe le module pour tester mes classes
 """
 
rect = moncode.Rectangle(4,1)
cerc = moncode.Cercle(2)
tria = moncode.Triangle(4, 4, 6)

class TestModule(unittest.TestCase):
    
    def test_rectangle(self):
        self.assertEqual(rect.getSurface(),4)
        self.assertEqual(rect.getCouleur(),'Blue')
        self.assertEqual(rect.getPerimetre(),10)        
        
    
    def test_carre(self):        
        self.assertTrue(cerc.getSurface(),12.566)
        self.assertTrue(cerc.getCouleur(),'Blue')
        self.assertTrue(cerc.getPerimetre(),4)
        
    def test_tria(self):
        self.assertEqual(tria.getSurface(),7.937)
        self.assertEqual(tria.getCouleur(),'Blue')
        self.assertEqual(tria.getPerimetre(),14)
        
        
if __name__=='__main__':
    unittest.main()
