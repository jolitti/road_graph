# This script will import a graph from a file and print out some useful stats for it

# by Marco


from sys import argv,getsizeof
import networkx as nx
from random import choice
import time
import math

def sizeofpaths(graph,*args,**kwargs):
    # get size in MBs
    print(graph)
    shortest_len_object = nx.single_source_dijkstra_path_length(graph,choice(list(graph.nodes)))
    size = getsizeof(shortest_len_object) // (1024*1024)
    return size

def timefun(fun,*args,**kwargs) -> tuple:
    # return seconds of execution and result
    start = time.time()
    result = fun(*args,**kwargs)
    end = time.time()
    return end-start,result

# read network file
assert len(argv)>=2, "Must specify a file containing a graph"
G = nx.read_adjlist(argv[1],nodetype=int)
graphsize = sum(getsizeof(v) for v in G.nodes) + sum(getsizeof(e) for e in G.edges)
graphsize = graphsize // (1024*1024)
print(f"Graph occupies {graphsize} MBs in memory")

print("Graph is connected" if nx.is_connected(G) else "Graph is not connected")

path_time,path_size = timefun(sizeofpaths,G)
print(f"The single source dijkstra path occupies {path_size} MB")
print(f"The calculation took {path_time} seconds")

# estimating the time needed to get a decent
# closeness centrality estimate
epsilon = 0.1
delta = 0.01
n = G.number_of_nodes()
k = math.ceil(
        (1/(2*(epsilon**2))) *
        (math.log(2*n / delta)) *
        (n / (n-1))**2
        )
print(f"A decent approximation of CC would take {k} iterations")
print(f"That's approximately {(k*path_time)/60} minutes")
