import reponse_7 as moncode
import unittest as ut


"""J'importe le fichier dans lequel se trouve nos classes
Rectangle,  Carre, Triangle,...
Et aussi J'importe le module pour tester mes classes
 """
 
rect = moncode.Rectangle(4,1)
cerc = moncode.Cercle(2)
tria = moncode.Triangle(4, 4, 6)
triRect =moncode.Triangle.Rectangle(4,9)

class TestModule(ut.TestCase):
    
    def test_rectangle(self):        
        self.assertEqual(rect.getSurface(),4)
        self.assertEqual(rect.getCouleur(),'Blue')
        self.assertEqual(rect.getPerimetre(),10)         
        self.assertNotEqual(rect.setCouleur("Blue"), "Rouge")
        
        
    
    def test_cercle(self):        
        self.assertTrue(cerc.getSurface(),12.566)
        self.assertTrue(cerc.getCouleur(),'Blue')
        self.assertTrue(cerc.getPerimetre(),4)
        self.assertNotEqual(cerc.setCouleur("Argent"), "Grise")

        
    def test_tria(self):
        self.assertEqual(tria.getSurface(),7.937)
        self.assertNotEqual(tria.getCouleur(),'Chocolat')
        self.assertEqual(tria.getPerimetre(),14)
        self.assertNotEqual(tria.setCouleur("Blue"), "Violet")
        
    def test_triRect(self):
        self.assertNotEqual(triRect.getSurface(),4)
        self.assertEqual(triRect.getCouleur(),"Blue")
        self.assertNotEqual(triRect.getPerimetre(),10)         
        self.assertNotEqual(triRect.setCouleur("Orange"), "Verte")
        

        
        
if __name__=='__main__':
    ut.main()
