import unittest # This module is comes with inbuild in python installation.
import Mathx
from Employee import Employe

# All the assert methods are present in unittest.TestCase class.

class Marvellous_Testing_Employee(unittest.TestCase):
    
    def setUp(self): # This method is used to use DRY policy of not making object of same class frequently. 
        self.obj1 = Employe("Kunal","Deshmane",13900)
        self.obj2 = Employe("Anurag","Deshmane",50000)
        
    def tearDown(self):
        pass

    def test_email(self):
        self.obj3 = Employe("Pavan","Gulve",20000)
        
        self.assertEqual(self.obj1.email,"Kunal.Deshmane@email.com")
        self.assertEqual(self.obj2.email,"Anurag.Deshmane@email.com")
        
        self.obj1.First = "Keshav"
        self.obj2.First = "Bharti"

        self.assertEqual(self.obj1.email,"Keshav.Deshmane@email.com")
        self.assertEqual(self.obj2.email,"Bharti.Deshmane@email.com")

    def test_fullname(self):

        self.assertEqual(self.obj1.Fullname,"Kunal Deshmane")
        self.assertEqual(self.obj2.Fullname,"Anurag Deshmane")

        self.obj1.First = "Keshav"
        self.obj2.First = "Bharti"

        self.assertEqual(self.obj1.Fullname,"Keshav Deshmane")
        self.assertEqual(self.obj2.Fullname,"Bharti Deshmane")

if __name__ == "__main__":
    unittest.main()
    
# If you don't want to write the unittest.main() method using starter then use below command.
#   python -m unittest file_name.py
# or if you write the unittest.main() method using starter then simply run below command.
#   python file_name.py

class Marvellous_Testing_Mathx():

    def test_add(self):
        self.assertEqual(Mathx.Add(10,5),15)
        self.assertEqual(Mathx.Add(5,5),10)
    
    def test_sub(self):
        self.assertEqual(Mathx.Sub(10,5),5)
        self.assertEqual(Mathx.Sub(5,5),0)
    
    def test_Mult(self):
        self.assertEqual(Mathx.Multi(10,5),50)
        self.assertEqual(Mathx.Multi(5,5),25)
    
    def test_Div(self):
        self.assertEqual(Mathx.Division(10,5),2)
        self.assertEqual(Mathx.Division(-1,-1),1)

        self.assertRaises(ValueError,Mathx.Division,10,2)

        # or we can do like this.

        with self.assertRaises(ValueError):
            Mathx.Division(10,0)