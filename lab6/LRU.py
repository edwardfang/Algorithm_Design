import collections

class LRUCacheItem(object):
    """Data structure of items stored in cache"""
    def __init__(self, key, value):
        # here we just set the key = value, in the more advanced case, we shall use the hash value
        self.key = key
        self.value = value

# Algorithm 1
class LRUCache(object):
    """A sample class that implements LRU algorithm"""

    def __init__(self, length):
        self.length = length
        self.hash = {}
        self.item_list = []
        self.hit = 0
        self.load = 0

    def loadItem(self, item):
        """Insert new items to cache"""

        if item.key in self.hash:
            # Move the existing item to the head of item_list.
            item_index = self.item_list.index(item)
            self.item_list[:] = self.item_list[:item_index] + self.item_list[item_index+1:]
            self.item_list.insert(0, item)
            self.hit += 1
            self.load += 1
        else:
            # If this is a new item, just append it to
            # the front of item_list.
            self.hash[item.key] = item
            self.item_list.insert(0, item)
            # Remove the last item if the length of cache exceeds the upper bound.
            if len(self.item_list) > self.length:
                self.removeItem(self.item_list[-1])
                self.load+=1



    def removeItem(self, item):
        """Remove those invalid items"""
        #print("Del",item.key)
        del self.hash[item.key]
        del self.item_list[self.item_list.index(item)]

    # get the string to show the update
    def getStatusString(self):
        s = "==================Ordinary====================\n"
        for x in range(1,self.length+1):
            s += "block"+ str(x)+"\t"
        s+="\n"
        for x in self.item_list:
            s += x.value+ "\t\t"
        s += "\n Hit Ratio: " + str(self.hit/self.load)
        return s

class LRUCache_new(object):
    def __init__(self, length,ratio):
        self.length = length
        self.hash = {}
        self.item_list = []
        self.oldstart = int((1-ratio) * length)
        self.pointer = 0
        self.hit = 0
        self.load = 0

    def loadItem(self, item):
        """Insert new items to cache"""
        if item.key in self.hash:
            # Move the existing item to the head of item_list.
            item_index = self.item_list.index(item)
            self.item_list[:] = self.item_list[:item_index] + self.item_list[item_index+1:]
            self.item_list.insert(0, item)
            self.load +=1
            self.hit +=1
        else:
            #print(self.pointer)
            if self.pointer<self.oldstart:
                self.hash[item.key] = item
                self.item_list.insert(0,item)
                self.pointer += 1
            elif self.pointer<self.length:
                self.hash[item.key] = item
                self.item_list.insert(self.oldstart,item)
                self.pointer += 1
            else:
                # If this is a new item, just append it to
                # the front of old.
                self.hash[item.key] = item
                self.item_list.insert(self.oldstart, item)
                # Remove the last item if the length of cache exceeds the upper bound.
                self.removeItem(self.item_list[-1])
                self.load+=1
    def removeItem(self, item):
        """Remove those invalid items"""
        #print("Del",item.key)
        del self.hash[item.key]
        del self.item_list[self.item_list.index(item)]

    # get the string to show the update
    def getStatusString(self):
        s = "==================Optimized====================\n"
        for x in range(1,self.length+1):
            s += "block"+ str(x)+"\t"
        s+="\n"
        for x in self.item_list:
            s += x.value+ "\t\t"
        s += "\n Hit Ratio: " + str(self.hit/self.load)

        return s