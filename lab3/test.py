from lab3 import BFS
import unittest

class MyTest(unittest):
    def test(self):
        graph = BFS.graphInput()
        print('Non-weighted Graph')
        print(graph.getFormattedResult(False))
        print('Weighted Graph')
        print(graph.getFormattedResult(True))