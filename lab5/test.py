from lab5.MST import Graph

import unittest,os

#[bonus] unittest!
class Mytest(unittest.TestCase):
    def test_input(self):
        f = open(os.path.dirname(os.path.realpath(__file__)) + '\\input.txt')
        g = Graph(f.read())
        f.close()
        x=g.primMST()
        y = g.KruskalMST()
        print("===============Input Graph==================")
        print(g.toString())
        print("================PrimMST=====================")
        print(x.toString())
        print("===============KruskalMST==================")
        print(y.toString())
if __name__ == '__main__':
    unittest.main()