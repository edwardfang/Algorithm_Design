import math,copy,random

class ClosestPair:
    def __init__(self, inputPointList):
        self.Px = sorted(inputPointList,key=lambda point: point[0])
        self.Py = sorted(inputPointList,key=lambda point: point[1])
        self.Pz = sorted(inputPointList,key=lambda point: point[2])


    def __closestPairRec(self,Px,Py,Pz):
        if len(Px) is 3:
            d1 = ClosestPair.__getdistance(Px[0],Px[1])
            d2 =  ClosestPair.__getdistance(Px[1],Px[2])
            d3 = ClosestPair.__getdistance(Px[0], Px[2])
            if d1<d2 and d1<d3:
                return (Px[0],Px[1])
            elif d2<d1 and d2<d3:
                return  (Px[1],Px[2])
            else:
                return  (Px[0],Px[2])
        elif len(Px) is 2:
            return (Px[0],Px[1])
        elif len(Px) is 1:
            return None
        #print("Px",Px)
        mid = int(len(Px)/2)
        Qx = Px[0:mid]
       # print("Qx",Qx)
        x_star = Qx[-1][0]
        for p in Px[mid:]:
            if p[0] is x_star:
                Qx.append(p)
                mid += 1
        Rx = Px[mid:]
        #print("Q",Qx,"R",Rx)
        Qy = sorted(Qx,key=lambda point: point[1])
        Ry = sorted(Rx,key=lambda point: point[1])
        Qz = sorted(Qx,key=lambda point: point[2])
        Rz = sorted(Rx,key=lambda point: point[2])
        x = self.__closestPairRec(Qx,Qy,Qz)
        #print("q part result",x)
        y = self.__closestPairRec(Rx, Ry, Rz)
        #print("r part result", y)
        if x is None:
            return y
        if y is None:
            return x
        (q0, q1) = x
        (r0, r1) = y
        d0 = ClosestPair.__getdistance(q0,q1)
        d1 = ClosestPair.__getdistance(r0,r1)
        if d0 < d1 :
            delta = d0
            pair_min = (q0,q1)
        else:
            delta = d1
            pair_min = (r0, r1)
        #print("delta before merge", delta)

        (P1,P2) = self.__constructP1P2(Px,Py,Pz,x_star,delta)
        for (_p,s) in P1:
            #print("_p",_p,"s",list(s))
            for (yindex, zindex) in s:
                min = zindex - 1
                if zindex is 0:
                    min = 0
                max = min + 2
                if zindex is len(P2[yindex]):
                    max = len(P2[yindex])
                #print("y",yindex,"minmax",min,max)
                #print(P2[yindex][min:max])
                for p_ in P2[yindex][min:max]:
                    #if _p
                    #print("cmp", _p, p_)
                    if ClosestPair.__getdistance(_p,p_) < delta:
                        delta = ClosestPair.__getdistance(_p,p_)
                        pair_min = (_p,p_)
        #print(pair_min,delta)
        return pair_min


    def __constructP1P2(self,Px,Py,Pz,x_star,delta):
        y_min = Py[0][1]
        y_max = Py[-1][1]
        blocknum = int((y_max-y_min)/(2*delta)+1)
        #print("blocknum",blocknum,"delta",delta,"Pz",Pz,"x_star",x_star)
        P1 = list()
        P2 = [list() for i in range(blocknum)]
        # print("P2",P2)
        for p in Pz:
            # P1 left part
            # print(p)
            if p[0]-x_star > -delta and p[0] <= x_star:
                s = list()
                if p[1]-y_min < delta:
                    s.append(0)
                elif y_max - p[1] <= 2*delta:
                    s.append(blocknum-1)
                else:
                    loc = int((p[1]-y_min-delta)/(2*delta))
                    s.append(loc)
                    s.append(loc+1)
                #print("s",s)
                zindex = list()
                for index in s:
                    if P2[index] is not []:
                        zindex.append(len(P2[index]))
                search = [(x,y) for (x,y) in zip(s,zindex) ]
                P1.append((p, search))
            # P2 right part
            if p[0] - x_star <= delta and p[0] > x_star:
                # print("P2_add",p,P2)
                loc = int((p[1]-y_min)/(2*delta))
                P2[loc].append(p)
        return (P1,P2)


    @staticmethod
    def __getNewSorted(list,keyindex):
        newlist = copy.copy(list)
        newlist.sort(key=lambda p:p[keyindex])
        return newlist

    @staticmethod
    def __getdistance(p1,p2):
        return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)

    def getPair(self):
        #(p0,p1) = self.__closestPairRec(self.Px,self.Py,self.Pz)
        pair = self.__closestPairRec(self.Px, self.Py, self.Pz)
        return (pair,ClosestPair.__getdistance(*pair))

if __name__ == '__main__':
    cp = ClosestPair([(2, 5, 9), (7, 3, 0), (2, 1, 6), (6, 2, 6), (9, 8, 6), (2, 0, 0), (5, 4, 7), (8, 8, 7), (3, 2, 3), (4, 3, 3)])
    print(cp.getPair())
    testlist = list()
    ## random test
    for i in range(100):
        testlist.append((random.randrange(1000),random.randrange(1000),random.randrange(1000)))
    cp = ClosestPair(testlist)
    print(cp.getPair())