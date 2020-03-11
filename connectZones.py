

# Program to connect communication zones
# Input :
# -1@10@-1#10@2@10#-1@10@-1
# 1@0@1#0@0@0#1@0@1
# -1@10@2@-1@-1#2@1@5@9@15#15@21@20@3@7#-1@5@9@20@30#-1@20@21@50@-1

import itertools  
class Graph:
 
    def __init__(self):
        rowList = []
        rowList = input().split("#")
        g = []
        for row in rowList:
            g.append([int(n) for n in row.split("@")])
        self.graph = g
        self.ROW = len(self.graph)
        self.COL = len(self.graph[0])

    def isSafe(self, i, j, visited):
        return (i >= 0 and i < self.ROW and
                j >= 0 and j < self.COL and
                not visited[i][j] and self.graph[i][j] == -1)

    def DFS(self, i, j, visited):
 
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
        colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]

        visited[i][j] = True
 
        for k in range(8):
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited):
                self.DFS(i + rowNbr[k], j + colNbr[k], visited)

    def countIslands(self):
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)]
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i][j] == False and self.graph[i][j] == -1:
                    self.DFS(i, j, visited)
                    count += 1
        return count

    def getRedZones(self):
        if (self.ROW >= self.COL):
            indexRange = self.ROW
        else: 
            indexRange = self.COL
        values = list(range(indexRange))
        redZones = []
        for p in itertools.product(values,repeat=2):
            p = list(p)
            if p[0] <=self.ROW and p[1]<=self.COL and self.graph[p[0]][p[1]] != -1:
                redZones.append(p)
        return (redZones)

    def permutateRedZones(self):
        redZones = []
        redZones = self.getRedZones()
        newCost = 999999999999       
        costList = []
        binString = ''
        # for flipRed in redZones:
        for i in range(0,2**len(redZones)):
            get_bin = lambda x, n: format(x, 'b').zfill(n)
            binString = get_bin(i, len(redZones))
            cost = 0
            for j in range(len(redZones)):
                if binString[j] == '1':
                    index = redZones[j]
                    costList.append(self.graph[index[0]][index[1]])
                    cost += self.graph[index[0]][index[1]]
                    self.graph[index[0]][index[1]] = -1
            if(self.countIslands() == 1):
                if(cost<newCost):
                    newCost = cost
            for j in range(len(redZones)):
                if binString[j] == '1':
                    index = redZones[j]
                    self.graph[index[0]][index[1]] = costList.pop(0)
        return newCost

g = Graph()
print(g.permutateRedZones())
