from lab4.topologicalSort import DAG
import unittest,os

#[bonus] unittest!
class Mytest(unittest.TestCase):
    def test_input(self):
        f= open(os.path.dirname(os.path.realpath(__file__))+'\\input.txt')
        g = DAG(f.read())
        f.close()
        g.topSort()
        g.topSort2()
        print('DFS_TopSort: ',[x.name for x in g.sortedList])
        print('Kahn_TopSort: ',[x.name for x in g.sortedList2])


if __name__ == '__main__':
    unittest.main()
