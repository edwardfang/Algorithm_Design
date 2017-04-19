from lab6.LRU import *
import unittest,os

#[bonus] unittest!
class Mytest(unittest.TestCase):
    def test_input(self):
        f = open(os.path.dirname(os.path.realpath(__file__)) + '\\input.txt')
        data = f.read()
        f.close()
        data = data.split("\n")
        lru1 = LRUCache(8)
        lru2 = LRUCache_new(8,0.375)
        cacheinput = dict()
        for line in data:
            n = line.split(" ")
            for x in n:
                if x not in cacheinput.keys():
                    cacheinput[x] = LRUCacheItem(x, x)
                print("Load",x)
                lru1.loadItem(cacheinput[x])
                lru2.loadItem(cacheinput[x])
            print(lru1.getStatusString())
            print(lru2.getStatusString())

if __name__ == '__main__':
    unittest.main()