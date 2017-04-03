import copy


class Node:
    def __init__(self, name):
        self.name = name


class DAG:
    ## default only positive adjacency input
    def __init__(self, DAGstring):
        self.adjList = dict()
        self.nodemap = dict()
        self.__processInput(DAGstring)
        self.__checkCycle()
        self.toadjListInverse()

    # [bonus] check cycle by DFS
    def __checkCycle(self):
        def hasCycleUtil(node):
            if node not in visited:
                visited.add(node)
                stack.add(node)
                if self.adjList[node] is not None:
                    for x in self.adjList[node]:
                        if (x not in visited and hasCycleUtil(x)):
                            return True
                        elif (x in stack):
                            return True
            stack.remove(node)
            return False

        for node in self.nodemap.values():
            stack = set()
            visited = set()
            if hasCycleUtil(node) is True:
                raise Exception('The DAG contains a cycle!')

    ## DFS
    def topSort(self):
        self.sortedList = list()
        visited = set()
        # find a outdegree 0 node
        zeroOut = set()

        def visit(node):
            if node not in visited:
                visited.add(node)
                for k, v in self.adjList.items():
                    if v is None:
                        continue
                    if (node in v):
                        visit(k)
                self.sortedList.append(node)

        for node in self.nodemap.values():
            if (self.adjList[node] is None):
                zeroOut.add(node)
        for x in zeroOut:
            visit(x)

    ## [bonus] another topSort
    def topSort2(self):
        stack = list()
        adji = copy.deepcopy(self.adjListInverse)
        self.sortedList2 = list()
        for node in adji.keys():
            if (adji[node] is None or len(adji[node]) is 0):
                stack.append(node)

        while stack:
            x = stack.pop()
            self.sortedList2.append(x)
            for k, v in adji.items():
                if(k not in stack and k not in self.sortedList2):
                    if x in v:
                        adji[k].remove(x)
                    if len(adji[k]) is 0:
                        stack.append(k)

    def toadjListInverse(self):
        self.adjListInverse = dict()
        for node in self.nodemap.values():
            tmp_list = list()
            for k, v in self.adjList.items():
                if (v is not None):
                    if (node in v):
                        tmp_list.append(k)
            self.adjListInverse[node] = tmp_list

    def __processInput(self, inputString):
        adjListData = inputString.split('\n')
        for x in adjListData:
            x = x.split(" ")
            if x[0] not in self.nodemap.keys():
                self.nodemap[x[0]] = Node(x[0])
            # add adjacency list for each nodw
            nodelist = list()
            if (len(x) > 1):
                for y in x[1:]:
                    if y in self.nodemap.keys():
                        nodelist.append(self.nodemap[y])
                    else:
                        self.nodemap[y] = Node(y)
                        self.adjList[self.nodemap[y]] = None
                        nodelist.append(self.nodemap[y])
            else:
                nodelist = None
            self.adjList[self.nodemap[x[0]]] = nodelist
