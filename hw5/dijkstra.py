import sys

def readGraph(filename):
    graph = {}
    nodes = {}
    with open(filename, 'r') as f:
        for line in f:
            tempArr = line.strip().split()
            nout = int(tempArr[0])
            nodes[nout] = 1
            if not nout in graph:
                graph[nout] = []
            for i in range(1, len(tempArr)):
                nin, weight = tempArr[i].split(",")
                graph[nout].append([int(nin), int(weight)])
                nodes[int(nin)] = 1
    return graph, len(nodes)
    
def dijkstra(graph, n, s):
    X = [s]
    A = {s:0}
    while len(X) != n:
        addNode = -1
        addA = sys.maxint 
        for nout in graph:
            if nout in X:
                for ninElem in graph[nout]:
                    if ninElem[0] not in X:
                        tempA = A[nout] + ninElem[1]
                        if tempA < addA:
                            addA = tempA
                            addNode = ninElem[0]
        if addNode == -1:
            break 
        X.append(addNode)
        A[addNode] = addA 
    return A 

def main():
    filename = sys.argv[1]
    graph, n = readGraph(filename)
    A = dijkstra(graph, n, 1)
    outArr = [7,37,59,82,99,115,133,165,188,197]
    s = ''
    for i in outArr:
        if i in A:
            s += str(A[i]) + ','
        else:
            s += '1000000,'
    
    print s 
    print A
    
if __name__ == "__main__":
    main()