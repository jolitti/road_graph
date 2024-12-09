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

params = [
        ("density",nx.density),
        ("assortativity",nx.degree_assortativity_coefficient),
        ("degree centrality",nx.degree_centrality),
        #("estrada index",nx.estrada_index), # not for undirected graphs
        #("trophic incoherence",nx.trophic_incoherence_parameter), # too spatially complex
        ("avg clustering",nx.average_clustering),
        #("avg node connectivity",nx.average_node_connectivity), # too long to compute
        #("harmonic diameter",nx.harmonic_diameter), # too long
        #("effective g res",nx.effective_graph_resistance), # too spatially complex
        #("kemeny const",nx.kemeny_constant), # too spatially complex
        #("global efficiency",nx.global_efficiency), # too long
        ]

for name,fun in params:
    secs,res = timefun(fun,G)
    print(f"Computing {name} took {secs:.2f} secs")
