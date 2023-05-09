import unittest
from greedy import greedy
from brute import knapSackFractional, knapSack01
from dynamic import dynamic
from Object import Object

class KnapSackTestCase(unittest.TestCase):    
    def setUp(self):
        self.box=[]
        self.size=20        
        obj1= Object("Object1", 25,18)
        obj2= Object("Object2", 24,15)
        obj3= Object("Object3", 15,10)
        self.box.append(obj1)
        self.box.append(obj2)
        self.box.append(obj3)

    def test_greedy(self):              
        output=greedy(self.box, self.size)
        expected=([{'name': 'Object2', 'profit': 24}, {'name': 'Object3', 'profit': 7.5}], 31.5)
        print(output)       
        self.assertEqual(output,expected)

    def test_dynamic(self):  
        obj0= Object("Object0", 0,0)  
        self.box.insert(0,obj0)          
        output=dynamic(self.box,self.size)
        expected=([{'name': 'Object1', 'profit': 25}], 25)
        print(output)       
        self.assertEqual(output,expected)

    def test_brute(self):  
        output=knapSack01(len(self.box), self.box, self.size, 0)
        expected=25
        self.assertEqual(output,expected)
        output=knapSackFractional(len(self.box), self.box, self.size, 0)
        expected= 31.5
        self.assertEqual(output,expected)


if __name__ == "__main__":
    unittest.main()    


    