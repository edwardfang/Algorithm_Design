from bitstring import *
import queue as Q
class CompressInfo:
    def __init__(self,map,remain):
        self.map = map
        self.remain = remain


class HNode:
    def __init__(self,data = None , leftchild = None, rightchild = None):
        self.data = data
        self.leftchild = leftchild
        self.rightchild = rightchild
        self.show = 1
        self.weight = 0
        self.code = None

    def count(self):
        self.show+=1
    def updateWeight(self,total):
        self.weight=self.show/total

    def __cmp__(self, other):
        if self.weight<other.weight:
            return -1
        elif self.weight>other.weight:
            return 1
        else:
            return 0
    def __lt__(self, other):
        if self.weight<other.weight:
            return True
        else:
            return False

class Encoder:
    def __init__(self,filename=None):
        if filename:
            self.filename = filename
            self.encode()
            self.bs = BitArray(self.binaryfile)
            print(self.bs.length)
    def encode(self):
        fp = open(self.filename, 'rb')
        self.binaryfile = fp.read()
        fp.close()


    def __genhuffmanT(self):
        # Main algorithm
        pq = Q.PriorityQueue(self.cnum)

        for key,node in self.bitset.items():
            node.updateWeight(self.cnum)
            pq.put(node)
            # only for debugging
            # print(node.data,node.show,node.weight)

        while pq.qsize() is not 1:
            e1 = pq.get()
            e2 = pq.get()
            #print(e1.data,e2.data)
            e = HNode(leftchild=e1,rightchild=e2)
            e.weight = e1.weight+e2.weight
            pq.put(e)
        self.root = pq.get()
        #print(root.leftchild.data)
        tranversal = Q.Queue()
        tranversal.put(self.root)
        self.root.code = BitArray()
        while(not tranversal.empty()):
            node = tranversal.get()
            if node.leftchild is not None:
                node.leftchild.code = node.code+BitArray(bin='0')
                tranversal.put(node.leftchild)
            if node.rightchild is not None:
                node.rightchild.code = node.code +BitArray(bin='1')
                tranversal.put(node.rightchild)

        # for key,node in self.bitset.items():
        #     # only for debugging
        #     print(node.data,node.show,node.weight,node.code.bin)

    def __encode(self):
        self.bitset = dict()
        self.cnum = self.bs.length/8

        # initialization
        for i in range(int(self.cnum)):
            bits = self.bs.bin[i * 8:i * 8 + 8]
            #print(bits)
            if bits not in self.bitset.keys():
                self.bitset[bits] = HNode(bits)
            else:
                self.bitset[bits].count()

        self.__genhuffmanT()


    def write(self,filename):
        self.__encode()
        out = BitArray('')
        for i in range(int(self.cnum)):
            bits = self.bs.bin[i * 8:i * 8 + 8]
            out+=BitArray(bin = self.bitset[bits].code.bin)
        self.remain = 8-out.length%8
        out+=BitArray(bin = '0'*self.remain)
        f= open(filename,'wb')
        f.write(out.bytes)
        print(out.length)
        map = dict()
        for key,value in self.bitset.items():
            map[Bits(value.code)] = key
        return CompressInfo(map,self.remain)

class Decoder:
    def __init__(self,filename,compreinfo):
        if filename:
            self.map = compreinfo.map
            self.remain = compreinfo.remain
            self.filename = filename
            self.decode()
            self.bs = BitArray(self.hfmfile)

    def __decode(self):
        tmp = BitArray()
        self.outbin = BitArray()
        #print(self.map.keys())
        #print(self.bs[0:20])
        for bit in self.bs.bin[0:-self.remain]:
            tmp+=BitArray(bin=bit)
            tmp_key = Bits(tmp)
            if tmp_key in self.map.keys():
                self.outbin += BitArray(bin = self.map[tmp_key])
                tmp.clear()
        print(self.outbin.length)
    def decode(self):
        fp = open(self.filename, 'rb')
        self.hfmfile = fp.read()
        fp.close()

    def write(self,filename):
        self.__decode()
        f = open(filename,'wb')
        f.write(self.outbin.bytes)


def main():
    huffman = Encoder("binaryfile.bin")
    huffman.encode()
    compreinfo = huffman.write("binaryfile.hfm")
    dehuffman = Decoder("binaryfile.hfm",compreinfo)
    dehuffman.write("out.bin")


if __name__ == '__main__':
    main()

