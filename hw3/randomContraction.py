import sys
import random
import time

def readGraphFromFile(filename):
    edgelist = []
    allnodes = {}
    with open(filename, 'r') as f:
        for line in f:
            tempArr = line.strip().split()
            firstElem = int(tempArr[0])
            allnodes[firstElem] = 1
            for i in range(1, len(tempArr)):
                adjacentElem = int(tempArr[i])
                allnodes[adjacentElem] = 1
                if firstElem < adjacentElem:
                    thisEdge = [firstElem, adjacentElem]
                    edgelist.append(thisEdge)
                    
    return edgelist, len(allnodes.keys())

def removeSelfLoop(edgelist):
    for i in xrange(len(edgelist)-1, -1, -1):
        if(edgelist[i][0] == edgelist[i][1]):
            del edgelist[i]
    
    
def randomMerge(edgelist):
    randi = random.randint(0, len(edgelist)-1)
    while(edgelist[randi][0] == edgelist[randi][1]):
        randi = random.randint(0, len(edgelist)-1)
    #print edgelist[randi]
    # merge the randi-th edge 
    tobemerged = edgelist[randi][1]
    mergeElem = edgelist[randi][0]
    #print tobemerged, mergeElem
    for edge in edgelist:
        if edge[0] == edge[1]: 
            continue 
        if edge[0] == tobemerged:
           # print "merged edge" + str(edge)
            edge[0] = mergeElem
        if edge[1] == tobemerged:
           # print "merged edge" + str(edge)
            edge[1] = mergeElem
        if edge[0] > edge[1]:
            temp = edge[1]
            edge[1] = edge[0]
            edge[0] = temp
    removeSelfLoop(edgelist)
            
def deepCopy(edgelist):
    result = []
    for edge in edgelist:
        temp = edge[:]
        result.append(temp)
    return result

def getTotalCut(edgelist, numNodes):
    thisEdgeList = deepCopy(edgelist)
    for i in range(numNodes - 2):
        randomMerge(thisEdgeList)
        
    result = 0
    for edge in thisEdgeList:
        if edge[0] != edge[1]:
            result += 1 
    return result 
    
def main():
    filename = sys.argv[1]
    edgelist, numNodes = readGraphFromFile(filename)
    print len(edgelist), numNodes
    numTrial = 1000
    results = []
    for i in range(numTrial):
        #random.seed(int(time.time()))
        results.append(getTotalCut(edgelist, numNodes))
    print "Results: "
    print results
    print "Minimun = " + str(min(results))
    
if __name__ == "__main__":
    main()
    