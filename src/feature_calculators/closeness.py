# Closeness centrality calculator
# by Marco

import networkx as nx
import math
import random

def calculate_feature(graph:nx.Graph,debug:bool=False) -> list[float]:
    # We will use the Eppstein-Wang algorithm
    # we assume an epsilon of 0.1 and a delta of 0.01 for our accuracy
    epsilon = 0.1 # relative deviation from real result
    delta = 0.01 # probability of any estimation being wronger than epsilon

    n = graph.number_of_nodes
    est_v = {n:0 for n in range(graph.number_of_nodes)} # generating may take a while

    # number of iterations
    k = math.ceil((1/(2*epsilon**2)) * math.log(2*n/delta) * ((n/(n-1))**2))

    if debug:
        print(f"performing {k} iterations of eppstein-wang")

    for i in range(k):
        if debug:
            print(f"Calculating iteration {i} out of {k}")
        random_node = random.randrange(0,n)
        distances = nx.single_source_dijkstra_path_length(graph,random_node)
        # TODO update est_v

    # TODO return average of est_v


    return []
