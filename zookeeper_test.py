import unittest
from zookeeper import Ztree

class TestZookeeper(unittest.TestCase):

    def test_crear_znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')

    def test_no_se_puede_crear(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1/node2/node3', 'algo', True, True, 10, None)
            
    def test_1_znode(self):
        tree = Ztree()
        tree.create('/node1', 'hola', True, True, 10, '/')   
        tree.create('/node2', 'que', True, True, 10, '/node1')
        tree.create('/node3', 'hace', True, True, 10, '/node2')
        self.assertEqual(tree.getData('/node1'), 'hola')
        self.assertEqual(tree.getData('/node2'), 'que')
        self.assertEqual(tree.getData('/node3'), 'hace')
        
    def test_2_znode(self):
        tree = Ztree()
        tree.create('/node1', 'hola', True, True, 10, '/')   
        tree.create('/node2', 'que', True, True, 10, '/')
        tree.create('/node3', 'hace', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'hola')
        self.assertEqual(tree.getData('/node2'), 'que')
        self.assertEqual(tree.getData('/node3'), 'hace')
        
    def test_3_znode(self):
        tree = Ztree()
        tree.create('/node1', 'hola', True, True, 10, '/')   
        tree.create('/node2', 'que', True, True, 10, '/node1')
        tree.create('/node3', 'hace', True, True, 10, '/node2')
        print(tree.delete('/node3',0))
        
    def test_4_znode(self):
        tree = Ztree()
        tree.create('/node1', 'hola', True, True, 10, '/')   
        tree.create('/node2', 'que', True, True, 10, '/node1')
        print(tree.delete('/node3',0))
        
    def test_5_znode(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1', 'hola', True, True, 10, '/')   
            tree.create('/node2', 'que', True, True, 10, '/node5')
            


if __name__ == '__main__':
    unittest.main()

