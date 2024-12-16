# Betweenness centrality calculator
# by Eddie

#import networkx as nx
import math
import random

import igraph as ig
import time        #to measure the time to compute features

def calculate_feature(graph:ig.Graph) -> list[float]:
    start = time.time()
    vertex_betweenness = graph.betweenness()
    end = time.time()
    print(vertex_betweenness)
    print("------------------------------------------------")
    print(end - start, "seconds")
    return []