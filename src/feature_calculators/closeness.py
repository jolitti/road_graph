# Closeness centrality calculator
# by Marco

import networkx as nx
import math

def calculate_feature(graph:nx.Graph) -> list[float]:
    # We will use the Eppstein-Wang algorithm
    # we assume an epsilon of 0.1 and a delta of 0.01 for our accuracy
    epsilon = 0.1 # relative deviation from real result
    delta = 0.01 # probability of any estimation being wronger than epsilon

    print("Calculating SSSP for one node")
    distances = nx.single_source_dijkstra_path_length(graph,0)
    print(distances)


    return [] # dummy output
