class Node:
    def __init__(self, name):
        self.name = name

class Graph:
    def __init__(self,GraphString = None):
        self.adjList = dict()
        self.maxweight = 0
        self.totalWeight = 0
        if(GraphString is not None):
            self.nodemap = dict()
            self.__processInput(GraphString)
        #print([(x.name,y[0][0].name) for (x,y) in self.adjList.items()])
    def __setTotalweight(self,weight):
        self.totalWeight = weight
    def __processInput(self,inputString):
        edgeData = inputString.split('\n')
        map = self.nodemap

        for data in edgeData:
            edge = data.split(' ')
            if(edge[1] not in map):
                map[edge[1]] = Node(edge[1])
            if (edge[0] not in map):
                map[edge[0]] = Node(edge[0])
        self.nodelist = list(self.nodemap.values())
        self.totalWeight = 0
        for data in edgeData:
            edge = data.split(' ')
            if(self.maxweight<int(edge[2])):
                self.maxweight = int(edge[2])
            self.totalWeight += int(edge[2])
            if(map[edge[1]] in self.adjList.keys()):
                self.adjList[map[edge[1]]].append((map[edge[0]],edge[2]))
            else:
                self.adjList[map[edge[1]]]=[((map[edge[0]], edge[2]))]
            if(map[edge[0]] in self.adjList.keys()):
                self.adjList[map[edge[0]]].append((map[edge[1]],edge[2]))
            else:
                self.adjList[map[edge[0]]]=[((map[edge[1]], edge[2]))]

    def addEdge(self,node1,node2,weight=0):
        self.totalWeight+=int(weight)
        if node1 not in self.adjList.keys():
            self.adjList[node1] = [(node2,weight)]
        else:
            self.adjList[node1].append((node2,weight))
        if(node2 not in self.adjList.keys()):
            self.adjList[node2] = [(node1,weight)]
        else:
            self.adjList[node2].append((node1,weight))

    def toString(self):
        s = "node\tadjacentNodes|weight\n"
        for (x,y) in self.adjList.items():
            s =s+ x.name
            for t in y:
                s = s +"\t"+ t[0].name+"|"+str(t[1])+" "
            s = s + "\n"
        s += "Total Weight:"+str(self.totalWeight)
        return  s

    def primMST(self):
        nodeset = set(self.nodelist)
        initset = set()
        initset.add(self.nodelist[0])
        #print([x.name for x in self.nodelist])
        newg = Graph()
        totalweight = 0
        while len(nodeset.difference(initset)) is not 0 :
            restset = nodeset.difference(initset)
            #print([x.name for x in initset])
            #print([x.name for x in restset])
            sourceNode = None
            nearestNode = None
            weight = self.maxweight
            for node in initset:
                for y in self.adjList[node]:
                    if y[0] in restset and int(y[1])<= weight:
                        sourceNode = node
                        nearestNode = y[0]
                        weight = int(y[1])
            #print(nearestNode.name)
            initset.add(nearestNode)
            newg.addEdge(sourceNode,nearestNode,weight)
        return newg



    def KruskalMST(self):
        edgelist = list()
        for (node1,adjlist) in self.adjList.items():
            for (node2,weight) in adjlist:
                if((weight,(node1,node2)) not in edgelist) and ((weight,(node2,node1))not in edgelist) :
                    edgelist.append((weight,(node1,node2)))
        edgelist.sort(key=lambda tup: tup[0])
        newg = Graph()
        count = 0
        for edge in edgelist:
            if count is len(self.nodemap)-1:
                break
            if edge[1][0] in newg.adjList.keys() and edge[1][1] in newg.adjList.keys():
                if count is not len(self.nodemap)-2:
                    continue

            newg.addEdge(edge[1][0],edge[1][1],edge[0])
            count+=1
        return newg



