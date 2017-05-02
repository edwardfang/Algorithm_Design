import  copy

class SortAndCount:
    def __init__(self,list):
        if len(list) < 2:
            raise Exception("length should be larger than 1")
        self.list = list
        self.count = 0
        self.sortedlist = list
        aux = copy.copy(list)
        self.count = self.__SortAndCount(list,0,len(list),aux)

    ## [bonus] optimized algorithm 1 and 2
    def __SortAndCount(self,list,lo,hi,aux):
        # print(list[lo:hi])
        if(hi<=lo+1):
            return 0
        mid = lo + int((hi-lo)/2)
        rA = self.__SortAndCount(aux,lo,mid,list)
        rB = self.__SortAndCount(aux,mid,hi,list)
        ## list: sorted in 2 parts respectively
        if(list[mid-1] <= list[mid]):
            r = 0
            aux[lo:hi] = list[lo:hi]
        else:
            r = self.__MergeAndCount(list,lo,mid,hi,aux)
        #print(rA,rB,r)
        return rA + rB + r

    def __MergeAndCount(self,list,lo,mid,hi,aux):
        r = 0
        i = lo
        j = mid
        x = lo
        # print("hi",hi,"lo",lo,"mid",mid)
        while i<mid  and j<hi:
            # print("i",i,"j",j,"mid",mid,"x",x)
            if list[i] <= list[j]:
                aux[x] = list[i]
                i += 1
            else:
                aux[x] = list[j]
                j += 1
                r += mid - i
            x += 1
        # print("gg","i", i, "j", j, "mid", mid, "x", x)
        if j is hi:
            #print(list[i+1:mid+1])
            aux[x:hi] = list[i:mid]
        else:
            aux[x:hi] = list[j:hi]
        list[lo:hi] = aux[lo:hi]
        # print("merge",aux,list)
        return r

    def getInversionnum(self):
        return self.count

