import math, queue
import os

class Graph:
    def __init__(self, nodeSet=None, edgeSet=None, source=None):
        if source is None:
            self.source = next(iter(nodeSet))
        else:
            self.source = source
        self.nodeSet = nodeSet
        self.edgeSet = edgeSet
        self.distance = dict()
        # generate the adjacency matrix
        self.adjacencyList = dict()
        if (nodeSet is not None):
            self.__generateDist()

        for node in nodeSet:
            nodelist = []
            for edge in edgeSet:
                if node is edge[0]:
                    if edge[1] not in nodelist:
                        nodelist.append(edge[1])
                if node is edge[1]:
                    if edge[0] not in nodelist:
                        nodelist.append(edge[0])
            self.adjacencyList[node] = nodelist
            # generate adjacency matrix
            self.adjacencyMatrx = dict()
            for v in nodeSet:
                for u in nodeSet:
                    d = 0
                    if (u, v) in edgeSet:
                        if nodeSet is None:
                            d = 1
                        else:
                            d = self.distance[(u, v)]

                    else:
                        d = 0
                    self.adjacencyMatrx[(u, v)] = d
                    self.adjacencyMatrx[(v, u)] = d

    # generate the distance map
    def __generateDist(self):
        s = self.nodeSet.copy()
        s_ = set()
        # x_distance=dict()
        distancePair = set()
        for x in s:
            if x not in s_:
                for y in s - {x}:
                    distancePair.add((x, y))
                s_.add(x)
        for (x, y) in distancePair:
            self.distance[(y, x)] = self.__calculateDist(x, y)
            self.distance[(x, y)] = self.__calculateDist(x, y)

    def __calculateDist(self, v1, v2):
        return math.sqrt((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2)

    # return a map<Node,distance> of dist and search path
    def getResult(self, has_weight):  # Algorithm_Design Algorithm here
        if (has_weight is False):
            path = []
            q = queue.Queue()
            q.put(self.source)
            path.append(self.source)
            distance = dict()
            distance[self.source] = 0
            i = 0
            while not q.empty():
                i += 1
                v = q.get()
                for u in self.adjacencyList[v]:
                    if u not in path:
                        path.append(u)
                        q.put(u)
                        distance[u] = i
            return path, distance
        elif self.nodeSet is not None:
            path = []
            q = queue.Queue()
            q.put(self.source)
            path.append(self.source)
            distance = dict()
            distance[self.source] = 0
            while not q.empty():
                v = q.get()
                for u in self.adjacencyList[v]:
                    if u not in path:
                        path.append(u)
                        q.put(u)
                        distance[u] = distance[v] + self.distance[(v, u)]
            return path, distance
        else:
            return None

    # Return formatted string as result
    def getFormattedResult(self, has_weight):
        path, distance = self.getResult(has_weight)
        fstring = 'The searching path is '
        tmp = ''
        for v in path:
            tmp = tmp + '-' + v.name
        fstring += tmp[1:]
        fstring += '\nThe distance is\n'
        for key, value in distance.items():
            fstring = fstring + key.name + '\t' + str(value) + '\n'
        return fstring

    def setSource(self, source):
        self.source = source


class Node:
    def __init__(self, name, x_offset, y_offset):
        self.name = name
        self.x = x_offset
        self.y = y_offset


# return a graph
def graphInput(filename=os.path.dirname(os.path.realpath(__file__))+'\\input.txt'):
    # parse the input file: 1 adjacency list; 2 offsets of vertex; 3 source point;
    f = open(filename)
    contents = f.read()
    contents = contents.split('\n\n')
    nodeData = contents[1].split('\n')
    edgeData = contents[0].split('\n')
    src = contents[2]
    nodeset = set()
    tmp_map = dict()

    for x in nodeData:
        x = x.split(' ')
        newNode = Node(x[0], int(x[1]), int(x[2]))
        tmp_map[x[0]] = newNode
        nodeset.add(newNode)

    # process the edge info into node tuple set
    edgeset = set()
    for x in edgeData:
        node = x.split(' ')
        for v in node[1:]:
            edgeset.add((tmp_map[node[0]], tmp_map[v]))

    return Graph(nodeset, edgeset, tmp_map[src])


if __name__ == "__main__":
    graph = graphInput()
    print('Non-weighted Graph')
    print(graph.getFormattedResult(False))
    print('Weighted Graph')
    print(graph.getFormattedResult(True))
