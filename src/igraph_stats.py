# This script will import a graph from a file and print out some useful stats for it
# (igraph version)

# by Marco


from sys import argv,getsizeof
from igraph import Graph
from random import choice
import time
import math

def timefun(fun,*args,**kwargs) -> tuple:
    # return seconds of execution and result
    start = time.time()
    result = fun(*args,**kwargs)
    end = time.time()
    return end-start,result

# read network file
assert len(argv)>=2, "Must specify a file containing a graph"
G = Graph.Load(argv[1],format="edgelist")
graphsize = sum(getsizeof(v) for v in G.vs) + sum(getsizeof(e) for e in G.es)
graphsize = graphsize // (1024*1024)
print(f"Graph occupies {graphsize} MBs in memory")

print(G.ecount())
print(G.get_edgelist()[0:10])

print("Graph is connected" if Graph.is_connected(G) else "Graph is not connected")

comps = G.connected_components()
print(max(comps.sizes()))
