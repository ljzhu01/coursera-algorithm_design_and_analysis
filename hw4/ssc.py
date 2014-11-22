import sys
import random

t = 0
s = 0 

def readGraph(filename):
    graph = {}
    rev_graph = {}
    nodes = {}
    with open(filename, 'r') as f:
        for line in f:
            node_out, node_in = line.strip().split()
            if not int(node_out) in graph:
                graph[int(node_out)] = []
            if not int(node_in) in rev_graph:
                rev_graph[int(node_in)] = []
            graph[int(node_out)].append(int(node_in))
            rev_graph[int(node_in)].append(int(node_out))
            nodes[int(node_in)] =1 
            nodes[int(node_out)] = 1
        
    return graph, rev_graph, len(nodes)

def dfs(G, i, f, leader, explored):
    explored[i-1] = True 
    leader[i-1] = s
    if i in G:
        for j in G[i]:
            if not explored[j-1]:
                dfs(G,j, f, leader, explored)
    global t 
    f[t] = i
    t += 1
    
def dfs_loop(G, f, n): 
    global s 
    global t
    t = 0
    s = None
    new_f = f[:]
    explored = [False] * n 
    leader = [0] * n 
    for i in range(n, 0, -1):
        # take node f[i-1]
        if not explored[f[i-1]-1]:
            s = f[i-1]
            dfs(G, f[i-1], new_f, leader, explored)
    return new_f, leader

def main():
    sys.setrecursionlimit(100000) # need to use stackless python
    filename = sys.argv[1]
    graph, rev_graph, n = readGraph(filename)
    # do the reverse dfs
    f = list(range(1, n+1))
    f, leader = dfs_loop(rev_graph, f, n)
    #print(f)
    #print(leader)
    f, leader = dfs_loop(graph, f, n)
    #print(f)
    #print(leader)
    sizes = {}
    for i in leader:
        if i not in sizes:
            sizes[i] = 0
        sizes[i] += 1
    sorted_sizes = sorted(sizes.values(), reverse=True)
    for i in range(5):
        if i < len(sorted_sizes):
            print(sorted_sizes[i])
        else:
            print(0)
            
            
if __name__ == "__main__":
    main()